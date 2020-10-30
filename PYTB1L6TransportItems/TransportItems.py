import os
import time
import sys

item = ("Battery")
emptylist = []
shop = []
distribution = []
factory = []
def Restart():
    print("Wil je het programma opnieuw uitvoeren? ('y' / 'n')")
    keuze = input(">>>> ")
    if(keuze == "y"):
        os.system('cls')
        Start()
    elif(keuze == "n"):
        exit()
    else:
        print("Typ alstublieft ('y' of 'n')")
        Restart()
        os.system('cls')

def Repeat(waarde, waarde1):
    waarde.append(item)
    waarde1.clear()
    time.sleep(.05)
    os.system('cls')

def PrintLists():
    print("Factory: ", factory)
    print("Distribution: ", distribution)
    print("Shop: ", shop)

def Start():
    os.system('cls')
    PrintLists()
    input()
    Repeat(factory, emptylist)
    #Factory heeft nu batterij
    PrintLists()
    input()
    Repeat(distribution, factory)
    #Distribution heeft nu batterij
    PrintLists()
    input()
    Repeat(shop, distribution)
    #Shop heeft nu batterij
    PrintLists()
    input()
    Repeat(emptylist, shop)
    #Batterij is nu verkocht
    PrintLists()
    print("\n" + "Je item is verkocht!\n")
    Restart()
Start()
