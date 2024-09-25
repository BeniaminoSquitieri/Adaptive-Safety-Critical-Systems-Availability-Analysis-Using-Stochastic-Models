from Subsystem import *
from build import *

if __name__ == "__main__":
    #costruzione del sistema ridondante con S1, S2, S3 ognuno con il proprio grado di ridondanza, ottenuto nell'analisi precedente. 
    S1_RED_NUM = 2 #grado di ridondanza del sistema S1
    S2_RED_NUM = 3 #grado di ridondanza del sistema S2
    S3_RED_NUM = 3 #grado di ridondanza del sistema S3
    
    #creazione dei sottosistemi
    S1 = Subsystem("S1", 0.2, 9.99610403e-001) 
    S2 = Subsystem("S2", 0.8, 9.98426217e-001)
    S3 = Subsystem("S3", 1, 9.98845783e-001)
    
    STEADY_STATE_DESIRED_AVAILABILITY = 0.999999 # soglia di disponibilità stazionaria
    
    # creazione del sistema complessivo tramite l’invocazione della funzione build_system che prende in input un dict di coppie key:value,
    # dove key rappresenta il sottosistema da inserire e value il numero di repliche
    system = build_system ({S1: S1_RED_NUM, S2 : S2_RED_NUM , S3: S3_RED_NUM})
    #Ottenuto quindi l’oggetto rappresentante l’intero sistema, è possibile passare 
    # alla definizione della configurazione che dovrà essere poi passata all’analyzer.
    
    
    #TRANSITION_NAME indica il nome della transizione temporizzata sotto analisi
    TRANSITION_NAME = 'lambda_DCK'
    #TRANSITION_VALUE_LOWER_BOUND indica il valore minimo in ore del valore minimo di MTTF o MTTR da associare alla transizione.
    TRANSITION_VALUE_LOWER_BOUND = 1
    #TRANSITION_VALUE_UPPER_BOUND indica il valore massimo in ore del valore minimo di MTTF o MTTR da associare alla transizione
    TRANSITION_VALUE_UPPER_BOUND = 1500
    #indica il passo con cui spostarsi dal lower bound all’upper bound
    TRANSITION_VALUE_STEP = 0.1
    configuration = {'TRANSITION_NAME': TRANSITION_NAME, 'TRANSITION_VALUE_LOWER_BOUND': TRANSITION_VALUE_LOWER_BOUND, 'TRANSITION_VALUE_UPPER_BOUND': TRANSITION_VALUE_UPPER_BOUND,'TRANSITION_VALUE_STEP': TRANSITION_VALUE_STEP, 'STEADY_STATE_DESIRED_AVAILABILITY': STEADY_STATE_DESIRED_AVAILABILITY}
    #Terminata la fase di configurazione, è stata invocata la funzione sensitivity_analyzer che prende in input come parametri: il sistema 
    # complessivo, il sottosistema sotto analisi, il file contenente l’opportuno codice sharpe per il calcolo della 
    # disponibilità stazionaria del sottosistema in esame e la configurazione precedentemente definita. Al termine della sua esecuzione,
    # tale funzione restituirà una lista di tuple del tipo (transition_value, new_availability, boolean_value). In particolare, boolean_value è uguale a
    # True per le coppie (transitizon_value, new_availability) in cui new_availability è al di sotto di quella fissata, False altrimenti.
    out = sensitivity_analyzer (system, S2, 'S2_steady_state_avail_config',configuration)
    TRANSITION_NAME = 'mu_DCK'
    TRANSITION_VALUE_LOWER_BOUND = 1/3600
    TRANSITION_VALUE_UPPER_BOUND = 20000/3600
    TRANSITION_VALUE_STEP = 0.5/3600
    configuration = {'TRANSITION_NAME': TRANSITION_NAME, 'TRANSITION_VALUE_LOWER_BOUND': TRANSITION_VALUE_LOWER_BOUND, 'TRANSITION_VALUE_UPPER_BOUND': TRANSITION_VALUE_UPPER_BOUND,'TRANSITION_VALUE_STEP': TRANSITION_VALUE_STEP, 'STEADY_STATE_DESIRED_AVAILABILITY': STEADY_STATE_DESIRED_AVAILABILITY}
    out = sensitivity_analyzer(system, S2, 'S2_steady_state_avail_config',configuration)