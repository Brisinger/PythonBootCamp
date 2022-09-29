# Function to recursively sum up first N natural numbers
def sum(n):
    if (n==1):
        return 1
    if (n<1):
        return None
    return sum(n - 1) + n

# Input the number
number = int(input("Enter a natural Number: "))
# Sum on first N natural numbers
print(f"Sum of {number} natural numbers", sum(number)) if (number>1) \
    else print(f"Sum of {number}st natural number", sum(number))