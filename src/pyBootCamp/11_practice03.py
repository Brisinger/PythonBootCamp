# Defining classes
"""
Class representing an Employee
"""
class Employee:
    def __init__(self, salary, increment) -> None:
        self.salary = salary
        self.increment = increment
    
    @property
    def salaryAfterIncrement(self):
        return self.salary * self.increment + self.salary
    
    @salaryAfterIncrement.setter
    def salaryAfterIncrement(self, value):
        if (value > 1200000):
            self.increment = 0.08
        else:
            self.increment = value
    
# Creating Employee objects
shubho = Employee(1200000, 0.01)
harry = Employee(1984000, 0.01)
# Display salary after increment
print(f"Salary of Shubho after increment", shubho.salaryAfterIncrement)
harry.salaryAfterIncrement = 0.05
print("Salary of Harry after increment",harry.salaryAfterIncrement)