from Subsystem import *
from analyzer import *
#implementazione della funzione build_system
#Inizializza un oggetto system di tipo SerieSubsystem, che rappresenta un insieme di sottosistemi collegati in serie. Successivamente, 
# itera attraverso ogni coppia chiave-valore nel dict configuration e, per ogni sottosistema, crea un ParallelSubsystem popolato con copie multiple del 
#sottosistema originale, basato sul valore associato nel dict. Allo stesso tempo, aggiorna il nome del sistema con una concatenazione dei nomi dei sottosistemi, restituendo, infine, l’oggetto system costruito, che ora rappresenta la struttura complessiva del sistema basato sulla configurazione fornita
def build_system (configuration : {Subsystem, int}):
    system = SerieSubsystem ('', [])
    name = ""
    for i, elem in enumerate (configuration.items()):
        key, value = elem
        temp = ParallelSubsystem (key.getName(), [])
        name += str (key.getName())
        for j in range (value):
            temp.addSubsystem (key)
            system.addSubsystem (temp)
        system.setName(temp)
    return system
