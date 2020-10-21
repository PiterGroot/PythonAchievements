import random

nametofind = "Waldo"

people = ["Waldo","Jackson","Ray","Eric","Vaughn","Jesse","Herbert","Robert", "Rodrigo","Elija","Sasha","Nathaniel","Ellie","Allison","Jeremiah", "Paula", "Alisha","Tory","Troy", "Faye"]
random.shuffle(people)

for value in people:
    print(value)

index = people.index(nametofind)
print("")
print("Anwser below:")
print("")
print('The index van', nametofind, 'in de lijst is:', index)

dontclose = input()
