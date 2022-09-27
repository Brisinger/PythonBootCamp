# Number entered by user
number = int(input("Enter the Number: "))
# Factorial of entered number
print("\nFactorial of", number, "is", end=" ")
for num in range(1, number):
    number = number * num
else:
    if (number==0):
        number = 1
        print(number)
    elif (number>0):
        print(number)
    else:
        print("undefined for negative integers")