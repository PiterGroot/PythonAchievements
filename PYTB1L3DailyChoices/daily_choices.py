import os
import sys


def q1():
    print("Het is half 7 in de avond, je hebt honger. Wat ga je doen?")
    print("")
    print(" A. Je besteld een pizza")
    print(" B. Je kijkt of er nog wat eten over van gisteren is")
    print(" C. Je slaat het eten over")
    a1 = input(" Kies 'A', 'B' of 'C' >>>>> ")
    if (a1 == "A"):
        print("")
        print("Je besteld van je laatste centen een pizza peperoni")
        print("")
    elif (a1 == "B"):
        print("")
        print("Je ziet nog wat pasta in de vriezer, je maakt dat klaar")
        print("")
    elif (a1 == "C"):
        print("")
        print("Je eet niks en je valt flauw, begin opnieuw")
        print("")
        q1()
    else:
        print("")
        print("Typ alstublieft A, B of C")
        print("")
        q1()
q1()

def q2():
    print("Er is een nieuwe game uit. Je wil het graag spelen, maar je bent ook moe. Wat ga je doen?")
    print("")
    print(" A. Je gaat de nacht doorhalen en de hele tijd de game spelen")
    print(" B. Je speelt de game 20 min en gaat dan slapen")
    print(" C. Je gaat gelijk slapen en morgen de game spelen")
    a2 = input(" Kies 'A', 'B' of 'C' >>>>> ")
    if (a2 == "A"):
        print("")
        print("De volgende dag val je in slaap tijdens je toets, je bent weggestuurd, begin opnieuw")
        print("")
        q2()
    elif (a2 == "B"):
        print("")
        print("Je wil eigenlijk door gamen maar je bent verstandig en gaat naar bed")
        print("")
    elif (a2 == "C"):
        print("")
        print("Je laat je niet verleiden door de game, echte dicipline!")
        print("")
    else:
        print("")
        print("Typ alstublieft A, B of C")
        print("")
        q2()
q2()

def q3():
    print("Je ziet een kans om tijdens de toets te spieken, wat ga je doen?")
    print("")
    print(" A. Je gaat het niet doen, je hebt goed geleerd")
    print(" B. Je pakt de kans en je spiekt bij je buurman")
    print(" C. Je doet net alsof je je pen laat vallen en kijkt dan snel voor antwoorden")
    a3 = input(" Kies 'A', 'B' of 'C' >>>>> ")
    if (a3 == "A"):
        print("")
        print("Goede keuze, alleen je hebt een onvoldoende haha")
        print("")
    elif (a3 == "B"):
        print("")
        print("Je spiekt, maar je word ondekt door je docent, oei oei. Begin opnieuw")
        print("")
        q3()
    elif (a3 == "C"):
        print("")
        print("Het lukt je, maar je valt kijhard. Dat wordt 6 weken in het gips, begin opnieuw")
        print("")
        q3()
    else:
        print("")
        print("Typ alstublieft A, B of C")
        print("")
        q3()
q3()

def q4():
    print("Je gaat naar huis, wat ga je doen?")
    print("")
    print(" A. Je pakt de bus")
    print(" B. Je pakt de fiets")
    print(" C. Je gaat te voet")
    a4 = input(" Kies 'A', 'B' of 'C' >>>>> ")
    if (a4 == "A"):
        print("")
        print("Goede keuze, alleen je valt in slaap en je stapt 10 km verder pas uit, begin opnieuw")
        print("")
        q4()
    elif (a4 == "B"):
        print("")
        print("Je fiets naar huis")
        print("")
    elif (a4 == "C"):
        print("")
        print("Je loopt langzaam naar huis")
        print("")
    else:
        print("")
        print("Typ alstublieft A, B of C")
        print("")
        q4()
q4()

def q5():
    print("Je gaat naar huis, wat ga je doen?")
    print("")
    print(" A. Je pakt de bus")
    print(" B. Je pakt de fiets")
    print(" C. Je gaat te voet")
    a5 = input(" Kies 'A', 'B' of 'C' >>>>> ")
    if (a5 == "A"):
        print("")
        print("Goede keuze, alleen je valt in slaap en je stapt 10 km verder pas uit, begin opnieuw")
        print("")
        q5()
    elif (a5 == "B"):
        print("")
        print("Je fiets naar huis")
        print("")
    elif (a5 == "C"):
        print("")
        print("Je loopt langzaam naar huis")
        print("")
    else:
        print("")
        print("Typ alstublieft A, B of C")
        print("")
        q5()
q5()

def q6():
    print("Je bent klaar")
    print("Wil je dit programma opnieuw starten (y / n)")
    dontclose = input()
    if(dontclose == "y"):
        os.execl(sys.executable, '"{}"'.format(sys.executable), *sys.argv)
    elif(dontclose == "n"):
        sys.exit()
    else:
        print("Typ alstublieft 'y' of 'n' in")
q6()
