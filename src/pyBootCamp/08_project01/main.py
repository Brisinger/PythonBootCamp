import random



def Game(compChoice, userChoice, choice):
    userChoice = userChoice.lower().strip()
    if (compChoice == choice[0]) and (userChoice == choice[2]):
        return True
    elif (compChoice == choice[1]) and (userChoice == choice[0]):
        return True
    elif (compChoice == choice[2]) and (userChoice == choice[1]):
        return True
    elif (compChoice == userChoice):
        return None 
    else:
        return False
    

choice = ('snake', 'water', 'gun')
# Choice by computer
comp = choice[random.randint(0, 2)]
# User's choice
user = input("Choose either snake, water or gun: ")

# Determining the winner
if (user in choice):
    win = Game(comp, user, choice)
    print(f"You chose {user} and computer chose {comp}")
    if win is None:
        print("Match is Drawn")
    elif win:
        print("You win!")
    else:
        print("You lose!")
else:
    print(f"Your choice {user} is invalid")
