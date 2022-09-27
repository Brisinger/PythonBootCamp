num = int(input("Enter Number: "))
# Multiplication table of user entered number
print("Multiplication table of", num)
counter = 1
while (counter < 13):
    print(f"{num} X {counter} = {num * counter}")
    counter += 1
else:
    print(f"\nMultiplication table for {num} listed successfully")