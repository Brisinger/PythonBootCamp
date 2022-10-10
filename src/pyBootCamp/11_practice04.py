# Defining classes for complex numbers
class Complex:
    def __init__(self, a, b) -> None:
        self.a = a
        self.b = b

    # Add complex numbers objects by overloading + operator
    def __add__(self, obj):
        result = Complex(self.a + obj.a, self.b + obj.b)
        return result

    # Multiply Complex number objects by overloading * operator
    def __mul__(self, obj):
        return Complex(self.a * obj.a + self.b * obj.b * -1, self.a * obj.b + self.b * obj.a)

    # Override string method of complex object
    def __str__(self) -> str:
        return str(self.a) + "+" + str(self.b) + "i"
    
# Creating Complex number objects
c1 = Complex(1, 4)
c2 = Complex(11, 3)

# Adding Complex number object
print(f"{c1} + {c2} = {c1 + c2}")
# Multiplying two Complex number objects
print(f"({c1}) * ({c2}) = {c1 * c2}")