# name = input("Enter your name:")
# print("Your name is:", name)

a = input("Enter the first number")
b = input("Enter the second number")

# Concatenates values as string instead of evaluating sum
print("\nConcatenates values entered as string instead of evaluating sum")
print("The Sum of {0} and {1} is: {2}".format(a, b, a + b))

# Calculates the sum instead of concatenating as strings
print("\nCalculates the sum of values entered instead of concatenating as strings")
print("The Sum of {0} and {1} is: {2}".format(a, b, int(a.strip()) + int(b.strip())))
