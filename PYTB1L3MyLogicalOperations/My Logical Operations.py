name = "erwin henraat"
job = "teacher"
moneyInAccount = 1300

#Vervang de ** met de logische operatoren 'and' en/of 'or'

#Zorg dat de if statement de functie buyABrandNewMotorcycle uitvoert als:
# Mijn naam erwin henraat is en ik een baan heb.
# Of als ik meer dan 10000 euro op mijn rekening heb staan.

def buyABrandNewMotorcycle():
    for index in range(1):
        print(":)")
        print("")

if name == "erwin henraat" and job != None or moneyInAccount > 10000:
    buyABrandNewMotorcycle()

school = "mediacollege"
isdocent = False
location = "Amsterdam"

def LetStudentIn():
    for index in range(1):
        print("We let you in :)")

if school == "mediacollege" and location == "Amsterdam" or isdocent == True:
    LetStudentIn()

dontclose = input()
#Maak nu voor jezelf ook een logische voorwaarde waarin je de operatoren 'and' en 'or' gebruikt.
