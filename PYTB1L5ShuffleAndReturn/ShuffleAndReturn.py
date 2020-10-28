import random

wordToShuffle = input("Typ een woord in >>>> ")

def shuffleWord(word):
        original = word
        randomised = ''.join(random.sample(original, len(original)))
        return randomised

for i in range(3):
    randomWords = shuffleWord(wordToShuffle)
    print(randomWords)


dontclose = input()
