'''
factorial(n) = factorial(n-1) * n, for n >= 1
               1, for n=0
'''
def factorial(n):
    # Base case of recursion
    if n==0:
        return 1
    if n<0:
        return None
    return factorial(n-1) * n
# Enter a number
number = int(input("Enter the Number: "))
# Displaying factorial of number from input
print("\nInvoking factorial() function")
print(f"Factorial of {number} is: {factorial(number)}")