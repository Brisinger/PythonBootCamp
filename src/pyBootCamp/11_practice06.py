# Defining classes
"""
Vector class of n dimentions with overriden string method for Vector objects
"""
class Vector:
    def __init__(self, n) -> None:
        if (isinstance(n, list)):
            for c in n:
                if not(isinstance(c, int)):
                    raise TypeError("Vector components must be integers")
            else:
                self.val = n
    
    @property
    def dimension(self):
        return len(self.val)
    
    def __str__(self) -> str:
        if (self.dimension == 3):
            return f"{self.val[0]}i + {self.val[1]}j + {self.val[2]}k"
        elif (self.dimension == 2):
            return f"{self.val[0]}i + {self.val[1]}j"
        else:
            return self.val

    def __add__(self, obj):
        dim = self.dimension
        n = []
        if (isinstance(obj, Vector)):
            for i in range(dim):
                n.insert(i, self.val[i] + obj.val[i])
            else:
                return Vector(n)
        else:
            raise TypeError(f"object must be of type {self.__class__.__qualname__} for addition operation")

    def __mul__(self, obj):
        dim = self.dimension
        n = 0
        if (isinstance(obj, Vector)):
            for i in range(dim):
                n += self.val[i] * obj.val[i]
            else:
                return n
        else:
            raise TypeError(f"object must be of type {self.__class__.__qualname__} for dot product operation")

# Creating objects of Vector with 3 dimensions
a = Vector([1, -8, 12])
b = Vector([2, 5, 4])

# Sum of Vector objects
sum = a + b
print(f"Adding vectors {a} and {b} is {sum}")

# Dot product of Vector objects
prod = a * b
print(f"Dot product of vectors {a} and {b} is {prod}")
