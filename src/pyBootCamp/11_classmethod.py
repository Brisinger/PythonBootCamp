# Defining class with class based methods
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


# Instantiate an Employee class
emp = Employee()
emp.a = Employee.a
emp.b = Employee.b
emp.setAttrs(1, 2, 3)
print(emp.a, emp.b, emp.c)
print(Employee.a, Employee.b, Employee.c)
