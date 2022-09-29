# Defining a function to find greater of three numbers
def greater(*args):
    greater = args[0]
    for num in args:
        greater = num if (num > greater) else greater
    return greater

# Set of numbers
numbers = set()
# Input three numbers
for i in range(3):
    numbers.add(int(input("Enter a Number: ")))
# List the greatest of three numbers
listOfNumbers = list(iter(numbers))
print(f"The greatest number among {listOfNumbers} is", \
    greater(*listOfNumbers))