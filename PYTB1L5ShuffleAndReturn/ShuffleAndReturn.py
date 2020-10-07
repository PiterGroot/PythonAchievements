import random

loop = 3
wordToShuffle = input("Typ een woord in >>>> ")


def shuffleWord(word):
        original = word
        randomised = ''.join(random.sample(original, len(original)))
        return randomised

for i in range(loop):
    randomWords = shuffleWord(wordToShuffle)
    print(randomWords)


dontclose = input()
