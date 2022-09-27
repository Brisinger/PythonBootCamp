# Input a natural number
N = int(input("Enter natural Number: "))
# Display first N natural numbers
print(f"\nFirst {N} natural numbers") if (N>1) else print(f"\nFirst natural number")
listOfNumbers = []
number = 1
while (number<N):
    print(f"{number}", end=", ")
    listOfNumbers.append(number)
    number += 1
else:
    if (number<=N):
        print(f"{number}", end="")
        listOfNumbers.append(number)
    else:
        print("\nThere are no natural numbers entered by user")

# Sum of first N natural numbers
print(f"\nSum of first {N} natural numbers:", sum(listOfNumbers, start=0)) if (N>1) \
    else print(f"\nSum of first natural number:", sum(listOfNumbers, start=0))