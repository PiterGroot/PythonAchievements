import random

loop = 3
wordToShuffle = input("Typ een woord in >>>> ")


def shuffleWord(word):
    for i in range(loop):
        original = word
        randomised = ''.join(random.sample(original, len(original)))
        print(randomised)

shuffleWord(wordToShuffle)

dontclose = input()
