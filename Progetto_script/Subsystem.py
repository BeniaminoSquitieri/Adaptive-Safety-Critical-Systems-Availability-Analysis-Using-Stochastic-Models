class Subsystem:
    #Rappresenta un sottosistema con nome, costo e disponibilità.
    
    def __init__ (self, name, cost , availability : float) : #costruttore per la classe Subsystem
        self.name = name #nome del sottosistema
        self.cost = cost #costo del sottosistema
        self.availability = availability #metrica di disponibilità del sottosistema come float
        
    def __str__ (self): 
        return self.name

    def __repr__(self):
        return self.name

    def setName (self, name): #setta il nome del sottosistema       
        if isinstance(name, str):  
            self.name = name
        
    def setCost (self, cost): #setta il costo del sottosistema
        if isinstance(cost, int) or isinstance(cost, float):
            self.cost = cost

    def setAvailability (self, availability): #setta la metrica di availability del sottosistema come float
       if isinstance(availability, int) or isinstance(availability, float):
           self.availability = availability
    #metodi getter per nome, costo e disponibilità del sottosistema
    def getName (self):
        return self.name

    def getCost (self):
        return self.cost

    def getAvailability (self):
        return self.availability

class SerieSubsystem(Subsystem): 
    #classe che eredita le caratteristiche della superclasse Subsystem ma con una funzionalità extra: l'aggiunta di un indice di serie
    def __init__(self, name, subsystems:  [Subsystem]) : #costruttore per la classe SerieSubsystem che ereditano le caratteristiche della superclasse Subsystem
    #Rappresenta una serie di sottosistemi che condividono lo stesso nome ma hanno differenti costi e metriche di disponibilità.
        self.subsystems = subsystems  #sottosistema
        temp_cost = 0 #costo del sottosistema
        temp_availability = 1 #metrica di disponibilità del sottosistema come float
        for subsystem in subsystems: #per ogni sottosistema
            temp_cost += subsystem.cost #incrementiamo il costo del sottosistema
            temp_availability *= subsystem.availability #incrementiamo la metrica di disponibilità del sottosistema come float
        super().__init__(name, temp_cost, temp_availability) #inizializzazione con i valori aggregati
        
    def addSubsystem (self, subsystem): #aggancia un sottosistema alla serie
            self.subsystems.append(subsystem) #aggiunge il subsystem
            self.cost += subsystem.cost #incrementiamo il costo del sottosistema
            self.availability *= subsystem.availability #incrementiamo la metrica di disponibilità del sottomodulo
        
    def removeSubsystem (self, subsystem): #rimuove un sottosistema dalla serie
            self.subsystem.remove (subsystem) #rimuove il subsystem
            self.cost -= subsystem.cost #decrementiamo il costo del sottosistema
            self.availability /= subsystem.availability #decrementiamo la metrica di disponibilità del sottosistema 
        
    def getSubsystems (self) -> [Subsystem]: #restituisce la lista di  tutti gli sottosistemi della serie
            return self.subsystems  
        
    def getAvailability (self): #restituisce la metrica di disponibilità del sottosistema come percentuale
            self.availability = 1
            for subsystem in self.subsystems: 
                self.availability *= subsystem.getAvailability()
            return self.availability
    
class ParallelSubsystem(Subsystem): #classe che modella un sottosistema parallelo
    #costruttore della classe ParallelSubsystem che modella un sottosistema parallelo
    def __init__(self, name, subsystems : [Subsystem]): #
        self.subsystems = subsystems #sottosistema
        temp_cost = 0 #costo del sottosistema parallelo
        temp_availability = 0 #metrica di disponibilità del sottosistema parallelo 
        for subsystem in subsystems : #per ogni sottosistema
            temp_cost += subsystem.cost #incrementiamo il costo del sottosistema parallelo
            temp_availability = 1 - (1 - subsystem.availability) #incrementiamo la metrica di disponibilità del sottosistema parallelo
        super().__init__(name, temp_cost , temp_availability) #inizializzazione con i valori aggregati
    # metodo che aggiunge un sottosistema alla serie parallelo aggiornando il costo totale e ricalcolando l'availability totale. 
    def addSubsystem (self, subsystem): 
        self.subsystems.append (subsystem)
        self.cost += subsystem.cost
        self.availability = 1 - (1 - self.availability) * (1 - subsystem.availability)
     # metodo che rimuove un sottosistema alla serie parallelo aggiornando il costo totale e ricalcolando l'availability totale. 
    def removeSubsystem (self, subsystem):
        self.subsystems.remove(subsystem)
        self.cost -= subsystem.cost
        self.availability = 1 -(1 - self.availability) / (1 - subsystem.availability)
    #restituisce la lista di tutti i sottosistemi nella configutazione in parallelo
    def getSubsystems (self) -> [Subsystem]:
        return self.subsystems
    # ricalcola e restituisce l'availability del sistema in parallelo
    def getAvailability(self):
        self.availability = 1 - (1 - self.subsystems[0].getAvailability())** len (self.subsystems)
        return self.availability

