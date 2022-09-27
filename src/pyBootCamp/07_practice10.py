# Enter a number from input
num = int(input("Enter Number: "))
# Multiplication table of user entered number
print("Multiplication table of", num)
for i in range(13, 0, -1):
    print(f"{num} X {i} = {num * i}")
else:
    print(f"\nMultiplication table for {num} listed successfully")