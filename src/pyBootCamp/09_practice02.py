import random
import os


# Define a function game to print random integes as score
def game():
    score = random.randint(1, 100)
    print(f"The score is {score}")
    return score

# Update the 09_practice02.txt file with highest score
# Check if file exits, if not create the file in give path
fileName = "09_practice02.txt"
path = os.path.join(fileName)
if not(os.path.exists(path)):
    with open(file=path, mode="w") as f:
        pass

with open(file="09_practice02.txt", mode="r") as f:
    text = f.read()
    hiscore = int(text) if (text != '') else game()
    score = game()
    if (score > hiscore):
        with open(file="09_practice02.txt", mode="w") as f:
            f.write(str(score))
