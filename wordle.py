import random
possibleWords = ["table", "shirt", "pants", "water", "knock"]
word = random.choice(possibleWords)

default = '\033[0m'
green = '\033[92m'
yellow = '\033[33m'

def gameloop():
    userGuess = ""
    for i in range(6):
        userGuess = input("Give me a guess: ")
        print(generateHint(userGuess))
        if(userGuess == word):
            print("You Won")
            break

def generateHint(guess):
    color = default
    hint = ""
    for i in range(5):
        if(guess[i] == word[i]):
            color = green
        elif(guess[i] in word):
            color = yellow
        else:
            color = default
        hint = hint + color + guess[i] + default
    return hint

gameloop()