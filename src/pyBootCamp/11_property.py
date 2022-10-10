# Defining class with class based methods and property and setter
'''
Class designating an Employee
'''
class Employee:
    a = 1
    b = 4
    c = 6

    @classmethod
    def setAttrs(cls, a, b, c):
        cls.a = a
        cls.b = b
        cls.c = c
    
    @property
    def length(self) -> int:
        return self.b

    @length.setter
    def length(self, value) -> int:
        self.b = value

# Instantiate an Employee class
emp = Employee()
emp.a = Employee.a
emp.b = Employee.b
emp.setAttrs(1, 2, 3)
print(emp.a, emp.b, emp.c)
print(Employee.a, Employee.b, Employee.c)
print(emp.length)
# Setting the property for Employee object
emp.length = 9
print(emp.length)

# Instantiating an Employee object
oldEmp = Employee()
print("Old employee length",oldEmp.length)