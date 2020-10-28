import os
import time


def Restart():
    print("Wil je het programma opnieuw uitvoeren? ('y' / 'n')")
    keuze = input(">>>> ")
    if(keuze == "y"):
        Start()
        os.system('cls')
    elif(keuze == "n"):
        exit()
    else:
        print("Typ alstublieft ('y' of 'n')")
        Restart()
        os.system('cls')
def Start():
    #Defineer lists en item
    item = ("Battery")
    shop = []
    distribution = []
    factory = []
    #print lege lists
    print("Factory: " + str(factory))
    print("Distribution: " + str(distribution))
    print("Shop: " + str(shop))
    makeItem = input()
    factory.append(item)
    time.sleep(.05)
    os.system('cls')
    #Factory heeft nu batterij
    print("Factory: " + str(factory))
    print("Distribution: " + str(distribution))
    print("Shop: " + str(shop))
    TransportItem = input()
    distribution.append(item)
    time.sleep(.05)
    factory.clear()
    os.system('cls')
    #Distribution heeft nu batterij
    print("Factory: " + str(factory))
    print("Distribution: " + str(distribution))
    print("Shop: " + str(shop))
    TransportItem = input()
    distribution.clear()
    time.sleep(.05)
    shop.append(item)
    os.system('cls')
    #Shop heeft nu batterij
    print("Factory: " + str(factory))
    print("Distribution: " + str(distribution))
    print("Shop: " + str(shop))
    buyItem = input()
    shop.clear()
    time.sleep(.05)
    os.system('cls')
    #Batterij is nu verkocht
    print("Factory: " + str(factory))
    print("Distribution: " + str(distribution))
    print("Shop: " + str(shop))
    print("\n" + "Je item is verkocht!")
    Restart()
Start()
