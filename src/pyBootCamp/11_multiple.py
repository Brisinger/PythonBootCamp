# Defining classes with multiple inheritance relationship
class Parent1:
    a = 4

class parent2:
    b = 2

class Child(Parent1, parent2):
    c = 9

# Create object instantiating child class
ch = Child()
print(ch.a)
print(ch.b)
print(ch.c)