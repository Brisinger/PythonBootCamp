# Defining classes with single inheritance relationship
'''
Employee
'''
class Employee:
    Company = "Microsoft"

'''
Programer who is an employee of Microsoft 
'''
class Programmer(Employee):
    Department = "Ecommerce"

    def __init__(self, name, language) -> None:
        self.name = name
        self.language = language
        super().__init__()
    
    def about(self):
        text = f"About {self.__class__.__name__} {self.name}\n"
        text += f"\tWorks for {self.Company} in {self.Department} Department.\n"
        text += f"\tDevelops software in {self.language}."
        return text

# Instantiating Programmer class with objects
harry = Programmer(name="Harry", language="Python")
shubho = Programmer(name="Shubhojit", language="Django")
# Displaying info about objects created.
print(harry.about())
print("\n")
print(shubho.about())
# Changing the department of shubho to Healthcare
print(f"\nChanging Department of {shubho.name} to Healthcare")
shubho.Department = "Healthcare"
# Display info about Shubhojit
print("Information related to", shubho.name + ":", f"\n{shubho.about()}")
# Display info about Harry
print("Information related to", harry.name + ":", f"\n{harry.about()}")

# Instantiating Employee class with objects
employee = Employee()
# Displaying attributes of Employee class
print(f"\nAttributes of {employee.__class__.__qualname__}:\n")
print(f"{dir(employee)}")
# Displaying attributes of Programmer class
print(f"\nAttributes of {harry.__class__.__qualname__}:\n")
print(f"{dir(harry)}")
