# Defining classes with multilevel inheritance relationship
class Parent:
    a = 4

class Child1(Parent):
    b = 2

class Child2(Child1):
    c = 9

# Create object instantiating Child2 class
ch = Child2()
print(ch.a)
print(ch.b)
print(ch.c)
# Displaying attributes of Child2 class object
print(f"\nAttributes of {ch.__class__.__qualname__}:\n")
print(f"{dir(ch)}")

# Create object instantiating Child1 class
ch = Child1()
# Displaying attributes of Child1 class object
print(f"\nAttributes of {ch.__class__.__qualname__}:\n")
print(f"{dir(ch)}")