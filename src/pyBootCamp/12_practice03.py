# Multiplication table of number entered by user
num = int(input("Enter a Number: "))

# List containing multiplication table
mul = [num * i for i in range(1, 13)]
print(mul)