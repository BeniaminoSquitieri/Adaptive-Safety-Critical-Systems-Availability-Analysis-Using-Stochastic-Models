from Subsystem import  Subsystem, SerieSubsystem
from Availability import AvailabilityOptimizer


if __name__ == "__main__":
    DESIRED_AVAILABILITY = 0.999999
    MAX_REDUNDANCY = 3
    S1 = Subsystem("S1", 0.2, 9.99610403e-001)  #9.99610403e-001
    S2 = Subsystem("S2", 0.8, 9.98426217e-001) #9.98426217e-001
    S3 = Subsystem("S3", 1, 9.98845783e-001)  # 9.98845783e-001

    
    net = SerieSubsystem("S1_S2_S3", [S1, S2, S3]) 
    opt_list = AvailabilityOptimizer.availabilityOptimizationAlgorithmRec(net,DESIRED_AVAILABILITY , MAX_REDUNDANCY)
    with open("lista_configurazioni_ottimali.txt", "w") as f:
        f.write("Configurazioni possibili per l'availability desiderata = " + str(DESIRED_AVAILABILITY) + " e massima ridondanza = " + str(MAX_REDUNDANCY) + "\n")
        for opt in opt_list:
            f.write("\nNome:" + str(opt))
            f.write("\nConfigurazione: [")
            for elem in opt.getSubsystems():
                f.write("(" + str(elem.getName()) + ", " + str(len(elem.getSubsystems())) + "), ")
            f.write("]")
            f.write("\nCosto: " + str(opt.getCost()) + "\n Disponibilita' stazionaria: " + str(opt.getAvailability()) + "\n")
    print("\nConfigurazioni possibili per l'availability desiderata scritte nel file lista_configurazioni_ottimali.txt:\n")
    optimal_configuration = AvailabilityOptimizer.getOptimalConfiguration(opt_list)
    print("\nConfigurazione con il costo minore\n Nome: " + str(optimal_configuration))
    print(" Configurazione: [", end="")
    for elem in optimal_configuration.getSubsystems():
        print("(" + str(elem.getName()) + ", " + str(len(elem.getSubsystems())) + "),", end="")
    print("]")
    print(" Costo: " + str(optimal_configuration.getCost()) +"\n Disponibilita' stazionaria: " + str(optimal_configuration.getAvailability()), end="\n\n")