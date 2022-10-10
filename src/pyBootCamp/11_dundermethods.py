# Defining class with operator overloading
class Employee:
    def __init__(self, a, name) -> None:
        self.a = a
        self.name = name
    
    def __add__(self, obj):
        return self.a + obj.a
    
    def __str__(self) -> str:
        return self.name

    def __len__(self):
        return len(self.name)

# Adding integers
print("Adding integers")
a = 45
b = 40
print(a + b)

# Adding class objects
print("Adding objects of class Employee")
emp1 = Employee(a, "Harry")
emp2 = Employee(b, "Shubhojit")
print(f"{emp1} + {emp2} = {emp1 + emp2}")
print(f"length of {emp1} and {emp2} together is", len(emp1) +len(emp2))