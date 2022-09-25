# Enter 4 numbers by user
import numbers


userCount = 4
print(f"Enter {userCount} numbers:")
numbers = []
for user in range(4):
    num = int(input("Enter a Number: "))
    numbers.append(num)
# List the largest number entered by 4 users using function on iterables
print("\nLargest number entered by user is:", max(numbers))
