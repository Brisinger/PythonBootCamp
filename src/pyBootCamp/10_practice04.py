# Defining calculator class
"""
Calculator class to compute square, cube and square root of a number
It also greets the user 
"""
class Calculator:
    def __init__(self, name, number) -> None:
        self.num = number
        self.name = name

    @staticmethod
    def greet() -> str:
        return "Greetings"

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
calc = Calculator(name="Shubhojit", number=number)
# Greet the user
print(f"{Calculator.greet()}! {calc.name},")
print(f"\tLet's play with {calc.num}.")
# Displaying square, cube and square root of the given number 
print(f"Square of {number} is {calc.square()}\nCube of {number} is {calc.cube()} and Square root of {number} is {calc.squareRoot()}")