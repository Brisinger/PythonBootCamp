# Defining classes with multilevel inheritance relationship
class Parent:
    a = 4

    def __init__(self) -> None:
        print(__class__.__qualname__)

class Child1(Parent):
    b = 2

    def __init__(self) -> None:
        print(__class__.__qualname__)
        super().__init__()

class Child2(Child1):
    c = 9

    def __init__(self) -> None:
        print(__class__.__qualname__)
        super().__init__()

# Creating object of class Child2
ch = Child2()