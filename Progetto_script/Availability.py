from Subsystem import *

class AvailabilityOptimizer:
    counter=0
    @staticmethod
    def availabilityOptimizationAlgorithmRec(subsystem, desired_availability=0.999999, max_redundancy=3):
        # metodo che implementa un algoritmo ricorsivo per ottimizzare la disponibilità del sottosistema .
        #La funzione ricorsiva trova la configurazione ottimale del sottosistema per ottenere la disponibilità desiderata.
        #Esplora iterativamente le differenti combinazioni di ridondanza di ogni sottosistema. I parametri che analizza sono: 
        #l'instanza del sottosistema serie da ottimizzare, l'availability desiderata e il massimo numero di ridondanza consentito per ogni sottosistema.
        #Ritorna una lista di configutrazioni, ognuna è una lista di tuple con un sottosistema e il suo costo di ridondanza.
        
        def recursiveOptimization(current_index, current_configuration, current_availability):
            if current_index == len(subsystem.subsystems):
                if current_availability >= desired_availability:
                    opt_list.append(AvailabilityOptimizer._buildConfiguration(current_configuration.copy()))
                return
            for redundancy in range(1, max_redundancy + 1):
                new_availability = 1 - (1 - subsystem.subsystems[current_index].availability) ** redundancy
                if current_index == 0:
                    updated_availability = new_availability
                else:
                    updated_availability = current_availability * new_availability

                current_configuration.append((subsystem.subsystems[current_index], redundancy))
                recursiveOptimization(current_index + 1, current_configuration, updated_availability)
                current_configuration.pop()
        opt_list = []
        recursiveOptimization(0, [], 1)
        return opt_list
        
    @staticmethod
    def getOptimalConfiguration (opt_list : [(Subsystem, int)]) -> [(Subsystem, int)]: # type: ignore
        #Questo metodoo statico determina la configurazione con il più basso costo da una lista di potenziali configurazioni. 
        #Questo metodo compara configurazioni differenti basate sul loro costo e ritorna quello con il costo migliore. 
        #In questo contesto i parametri che prende sono una lista di configurazioni potenziali e ritorna una tupla contenente la configurazione 
        #del sottosistema e le loro ridondanze rispettive. 
        if len (opt_list) == 0:
            return None
        else:
            best_configuration = opt_list [0]
            for configuration in opt_list:
                if configuration.getCost() < best_configuration.getCost():
                    best_configuration = configuration
            return best_configuration
        
    @staticmethod
    def _buildConfiguration (configuration) -> SerieSubsystem:
        #Metodo statico per costruitre un istanza di SerieSubsystem da una data configurazione.
        #Questo metodo costruisce un SerieSubsystem da una configurazione che specifica la ridondanza per ogni Subsystem nella serie.
        #In questo contesto i parametri che prende sono una lista di configurazioni(tuples) ognuna contenenti un Sottosistema e il suo indice di ridondanza.
        #Ritorna un istanza di SerieSubsystem rappresentando la configurazione specifica.
        
        serie_subsystem = SerieSubsystem ("" , [])
        name = ""
        AvailabilityOptimizer.counter += 1
        for subsystem, redundancy in configuration :
            parallel_subsystem = ParallelSubsystem("", [])
            for i in range(redundancy):
                parallel_subsystem.addSubsystem(Subsystem(str(subsystem), subsystem.getCost(), subsystem.getAvailability()))
                parallel_subsystem.setName(str(subsystem))
            name += str(subsystem) + "_"
            serie_subsystem.addSubsystem(parallel_subsystem)
        name += str(AvailabilityOptimizer.counter)
        serie_subsystem.setName(name)
        return serie_subsystem
    
    @staticmethod
    def availabilityOptimizationAlgorithm(subsystem : SerieSubsystem ,desired_availability = 0.999999, max_redundancy = 3) -> [(Subsystem , int)]:
    #Ottimizza la ridondnza di un sistema serie consistente esattamente di tre elementi chiave per raggiungere una availability desiderata.
    #Questo metodo statico calcola la ridondanza ottimale per ognuno dei tre sottosistemi in una configurazione serie per trovare l'availability desiderata.
    #La funzione itera lungo possibili libelli di ridondanza per ognuno dei sottosistemi e calcola l'availability totale del sistema. Il metodo è specificatamente designatoo
    #per sistemi composti di esattamente tre elementi ed è meno generico rispetto ad un approccio ricorsiva che gestisce i sisteemi con un numero arbitrario
    #di serie e parallelo. Notiamo che questo metodo è applicabile solamente ad instanze di SerieSubsystem con tre elementi.
    #I parametri che il metodo prende sono una lista di configurazioni di sottosistemi, che nel caso specifico sono tre, poi una disponibilità desiderata, per il 
    #sistema serie come float, la quale è impostata di default a 0.999999.Infine viene ritornata una lista di tuple , ognuna  contenenete un sottosistema ed il 
    #il suo livello di ridondanza , per raggiungere la disponibilità desiderata.
        opt_list = []
        for i in range(1, max_redundancy + 1):
            for j in range(1, max_redundancy + 1):
                for k in range(1, max_redundancy + 1):
                    avail_i = 1 - (1 - subsystem.subsystems[0].availability) ** i
                    avail_j = 1 - (1 - subsystem.subsystems[1].availability) ** j
                    avail_k = 1 - (1 - subsystem.subsystems[2].availability) ** k
                    if avail_i * avail_j * avail_k >= desired_availability:
                        opt_list.append([(subsystem.subsystems[0], i), (subsystem.subsystems[1], j), (subsystem.subsystems[2], k)])
        return opt_list



