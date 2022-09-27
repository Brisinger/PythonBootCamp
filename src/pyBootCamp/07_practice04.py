import math


# Get number from user
number = int(input("Enter the Number: "))

# Verify the number entered by user is prime number
for num in range(2, int(math.sqrt(number))):
    if (number % num) == 0:
        print(f"{number} is not prime")
        break
else:
    print(f"{number} is prime") if (number > 1) else print(f"{number} is not prime")
