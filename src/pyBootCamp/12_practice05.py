# Multiplication table of number entered by user
num = int(input("Enter a Number: "))

# List containing multiplication table
mul = [num * i for i in range(1, 13)]
print(mul)

# Storing the multiplication table list in a file
with open(file="12_practice05.txt", mode="w") as writer:
    writer.write(str(mul))