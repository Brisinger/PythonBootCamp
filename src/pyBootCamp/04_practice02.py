# Defining an empty set
from token import SOFT_KEYWORD


setOfNumbers = set()
# Fetch 8 numbers from user input
num =int(input("Enter the 1st number: "))
setOfNumbers.add(num)
num =int(input("Enter the 2nd number: "))
setOfNumbers.add(num)
num =int(input("Enter the 3rd number: "))
setOfNumbers.add(num)
num =int(input("Enter the 4th number: "))
setOfNumbers.add(num)
num =int(input("Enter the 5th number: "))
setOfNumbers.add(num)
num =int(input("Enter the 6th number: "))
setOfNumbers.add(num)
num =int(input("Enter the 7th number: "))
setOfNumbers.add(num)
num =int(input("Enter the 8th number: "))
setOfNumbers.add(num)

# Dislay the numbers entered.
print("\nThe unique numbers entered by user are", setOfNumbers)

