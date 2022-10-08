import sys


# Creating a class
class Employee:
    name = "Shubho"
    marks = 34
    center = "Delhi"

    def __repr__(self) -> str:
        return f"Employee {self.name}"
    
    def __str__(self) -> str:
        return self.name

shubho = Employee()
# Canonical string representation of object
print(f"Canonical representation: {repr(shubho)}")
# String representation of object
print(f"String representation: {str(shubho)}")
# Object details
print(repr(shubho), "has", shubho.marks, "marks from center", shubho.center)
# Object size
print(f"Size of {shubho} object: {sys.getsizeof(shubho)} bytes with name occupying\
    {sys.getsizeof(shubho.name)} bytes, marks {sys.getsizeof(shubho.marks)} bytes and\
    center occupying {sys.getsizeof(shubho.center)} bytes")
