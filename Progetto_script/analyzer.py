import os
from sys import stdout
from asyncio import *
import re
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.ticker import FormatStrFormatter
from Subsystem import *
import shutil
import subprocess
def sensitivity_analyzer (system, subsystem, filename, configuration):
    filename_temp = filename + '_temp' #creazione file temporaneo
    shutil.copy (filename, filename_temp) #copia dei dati del file originale in quello temporaneo 
    out_points = []  #inizializzazione lista vuota per la memorizzazione dei risultati. 
    #esecuzione di un ciclo for con passo di TRANSITION_STEP da TRANSITION_VALUE_LOWER_BOUND a TRANSITION_VALUE_UPPER_BOUND.
    for transition_value in np.arange (configuration ['TRANSITION_VALUE_LOWER_BOUND'], configuration ['TRANSITION_VALUE_UPPER_BOUND'], configuration ['TRANSITION_VALUE_STEP']):
        _update_file (filename_temp, configuration['TRANSITION_NAME'], transition_value) #aggiorniampo il file sharpe temporaneo con il nuovo valore di MTTF/MTTR 
        _compute_availability (subsystem, filename_temp) #calcoliamo la nuova disponibilità del sistema 
        new_availability = system.getAvailability () #otteniamo la nuova disponibilità del sistema
        if new_availability < configuration ['STEADY_STATE_DESIRED_AVAILABILITY']: #determiniamo se la nuova disponibilità del sistema è superiore o inferiore alla soglia desiderata
            out_points.append ((transition_value, new_availability, True)) #se inferiore alla soglia desiderata viene impostato il flag a True
        else:
            out_points.append ((transition_value, new_availability, False)) #altrimenti al valore False
    os.remove (filename_temp) # rimoviamo il file temporaneo 
    return out_points #restituzione della lista contenente i risultati delle analsi. 

def _update_file (filename, transition_name, transition_value):
    with open (filename, 'r') as f: #apre il file in modalità lettura e legge tutte le sue linee memorizzandole nella variabile "lines"
        lines  = f.readlines()
    for i, line in enumerate (lines): #effettua un'iterazione su ogni riga, controlla se ciascuna inziia con "transition_name".
        if line.startswith (transition_name): #In caso affermativo sostisuisce quella riga on una nuova stringa che contine il nome della transizione seguito da 1/ ed il nuovo 
            #valore di transition_value, ovvero MTTR/MMTF. 
            lines[i] = str(transition_name) + '1/' + str (transition_value) + '\n'  
    with open (filename, 'w') as f: #infine lo stesso file viene aperto in modalità di scrittura per scrivere tutte le linee, adesso aggionrate. 
        f.writelines(lines)
        
def _compute_availability  (subsystem, filename):
    file_path = filename  # Sostituisci questo con il nome effettivo del file
    absolute_path = os.path.abspath(file_path)
    print("Il percorso completo del file è:", absolute_path)
    process = subprocess.run([absolute_path], capture_output=True) #viene lanciato lo script SHARPE, usando il file precedentemente aggiornato con il nuovo valore di MTTF/MTTR 
    output = process.stdout 
    #stdout.decode ('utf-8') #poichè l'output catturato è in formato binario questo deve essere decodificato in una stringa UTF-8 per poter essere utilizzato. 
    match = re.search (r"SS_ExpectedrewardRate: \s*(\d\.e-)+", output) #Successivamente vengono utilizzati dei regex per cercare una stringa specifica nell'output in particolar modo quella indicante il nuovo valore di disponibilità calcolato. 
    value = match.group (1) if match else None #Viene quindi estretto il valore numerico 
    subsystem.setAvailability (float(value)) #e viene usato per aggiornare la disponibilità del sottosistema. 
    
#la funzione per plottare i grafici oltre a tracciare il grafico sulla base dei valori di output dell'analisi , inserisce sia una retta rappresentativa del valore nimnale del parametro considerato, sia un simbolo, 
#ovvero nel nostro caso una stela, rappresentante il punto che ha come ascissa il valore ceritico del parametro a partire dal quale la disponiblità stazionaria scende
#al di sotto di quella fissat e ecome orfinata il valroe della disponibilità stesso. Al fine diottenere tale punto critico la funzione plot si avvale della procedura 
#find_critical_index che trova l'indice del valore creitico nie risutlati dell'analisi di sensibilità. 
def plot (out, rate_type, nominal_value , title, x_label = "X-axis", y_label = "Y_axis", x_scale = "linear", y_scale = "linear"):
    x, y, z = zip(*out)
    x,y = list (x), list (y)
    plt.figure (figsize = (10, 6))
    plt.plot (x,y)
    plt.plot (np.ones_like(x) * nominal_value , y , linestyle = '--', color = 'yellow', label = 'Nominal value')
    critical_index = find_critical_index (z, rate_type)
    if critical_index is not None:
        x_critical, y_critical = x [critical_index], y [critical_index]
        print (x_critical, y_critical)
        plt.scatter (x_critical, y_critical, marker = '*', s= 300, c= 'red', label = 'Critical value = ' + str (x_critical) + "[h]")
        plt.ylim (y_critical - 0.0000010 , 0.999999)
    else:
        plt.ylim(0.999997740, 0.999999900)
        plt.title(title)
        plt.xlabel(x_label)
        plt.ylabel(y_label)
        ax = plt.gca()
        ax.set_xlabel(f"${x_label}$")
        ay = plt.gca()
        ay.set_ylabel(f"${y_label}$")
        plt.grid(True)
        plt.xscale(x_scale)
        plt.yscale(y_scale)
        plt.gca().yaxis.set_major_formatter(FormatStrFormatter('%.7f'))
        plt.legend()
        plt.savefig('Results' + os.sep + title + '.png')

def find_critical_index(lst, rate_type):
 if rate_type == 'failure':
    if lst[-1] == True:
        return len(lst)- 1
    for i, elem in enumerate(lst):
        if elem is False:
            return i- 1 if i > 0 else None
 elif rate_type == 'repair':
    for i, elem in enumerate(lst):
        if elem is True:
            return i
 return None