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
harry = Employee()
print(shubho)
print(harry)

# Changing class attribute values using objects of class
print("Changing value of an object")
harry.name = "Harry"
print(harry)
print(shubho)
print("Value of class attribute name",Employee.name)

