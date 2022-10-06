import random
import os


number = random.randint(1, 100)

def guessingGame(number, file):
    isNotMatch = True
    count = 0 

    while isNotMatch:
        count += 1
        guess = int(input("Guess the number: "))
        match guess:
            case _ if guess is number:
                print(f"Perfect guess of number {number} you win!")
                isNotMatch = False
            case _ if (guess < number):
                print("Guess a higher number")
            case _:
                print("Guess a lower number")
    else:
        print(f"\nYou guessed the number {number} in {count} guesses")
        hiscore = 0
        if os.path.exists(path=file):
            with open(file=file, mode="r") as f:
                hiscore = int(f.read().split(':')[1].strip())
    
        if (count<hiscore):
            print("You have just broken the high score!")
            with open(file, "w") as f:
                f.write(f"Total number of guesses: {count}\n")
        else:
            print(f"You have not broken the high score of {hiscore} guesses!")

# Input file to store results from user
fileName = input("Enter the file name to store game score: ")
# Play the game
print("Play the guessing game\n")
guessingGame(number, file=fileName)

