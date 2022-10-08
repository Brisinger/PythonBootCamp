# Defining calculator class
"""
Calculator class to compute square, cube and square root of a number 
"""
class Calculator:
    def __init__(self, number) -> None:
        self.num = number

    def square(self):
        return self.num * self.num
    
    def squareRoot(self):
        root = self.num / 2
        for n in range(7):
            root = root - ((root * root - self.num) / (2*root))
        return "%2.4f" % root

    def cube(self):
        return self.square() * self.num

# Input from user
number = int(input("Enter the Number: "))
# Create Calculator object
calc = Calculator(number)
# Displaying square, cube and square root of the given number 
print(f"Square of {number} is {calc.square()}, Cube of {number} is {calc.cube()} and Square root of {number} is {calc.squareRoot()}") 
            