num = int(input("Enter Number: "))
# Multiplication table of user entered number
print("Multiplication table of", num)
for i in range(1, 13):
    print(f"{num} X {i} = {num * i}")
else:
    print(f"\nMultiplication table for {num} listed successfully")