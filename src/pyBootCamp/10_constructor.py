# Defining a class with constructor
'''
Employee
'''
class Employee:
    Company = "Google" # class attribute
    def __init__(self, name, dept):
        # Instance attributes
        self.name = name 
        self.department = dept

    def getName(self):
        return self.name
    
    def getDepartment(self):
        return self.department

    def __str__(self) -> str:
        return self.getName() + "(" + self.getDepartment() + ")"
    
# Instantiating Employee class
shubho = Employee("Shubhojit", "Finance")
print(shubho, "works in", Employee.Company)
harry = Employee("Harry", "Site Reliability Engineer")
print(harry, "works in", Employee.Company)
    