# Class with class based attribute
class MyClass:
    a = 0

    def __str__(self) -> str:
        return __class__.__name__ + f"({self.a})"

# Instance of class MyClass
obj = MyClass()
print(obj)
# Modifying the value of class attribute using object
print("Modifying the class attribute 'a' value to 9 using object")
obj.a = 9
print(obj, "But class attribute a:", MyClass.a)
