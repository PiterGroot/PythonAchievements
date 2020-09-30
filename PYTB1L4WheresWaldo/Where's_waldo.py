import random

nametofind = "Waldo"

people = ["Waldo","Jackson","Ray","Eric","Vaughn","Jesse","Herbert","Robert", "Rodrigo","Elija","Sasha","Nathaniel","Ellie","Allison","Jeremiah", "Paula", "Alisha","Tory","Troy", "Faye"]
random.shuffle(people)

for value in people:
    print(value)

index = people.index(nametofind)
print("")
print("<-------------------------------------------------------->")
print('The index of', nametofind, 'in the list is:', index)

dontclose = input()
