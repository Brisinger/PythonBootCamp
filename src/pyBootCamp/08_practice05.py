# Function printing stars
def printPattern(n):
    for i in range(n, 0, -1):
        print("*"*i)
    else:
        print("\n")

# Enter number from user
number = int(input("Enter the Number: ")) 
# Invoking function printing the pattern
printPattern(number)