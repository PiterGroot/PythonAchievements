import random

wordToShuffle = input("Typ een woord in >>>> ")
loop = input("Hoevaak wil je je woord shuffelen? >>>> ")
loop = int(loop)

def shuffleWord(word):
        original = word
        randomised = ''.join(random.sample(original, len(original)))
        return randomised

for i in range(loop):
    randomWords = shuffleWord(wordToShuffle)
    print(randomWords)


dontclose = input()
