# Creating a class with static method
class Employee:
    name = "Shubho"
    marks = 34
    center = "Delhi"

    def __repr__(self) -> str:
        return f"Employee {self.name}"
    
    def __str__(self) -> str:
        return self.name

    @staticmethod
    def greet():
        return "Good day"

shubho = Employee()
harry = Employee()
print(shubho.greet(), shubho)
harry.name="Harry"
print(Employee.greet(), harry)