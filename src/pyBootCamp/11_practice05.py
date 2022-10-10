# Defining classes
"""
Vector class of n dimentions
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
        prod = 0
        if (isinstance(obj, Vector)):
            for i in range(dim):
                prod += self.val[i] * obj.val[i]
            else:
                return prod
        else:
            raise TypeError(f"object must be of type {self.__class__.__qualname__} for dot product operation")

# Creating objects of Vector with 3 dimensions
a = Vector([1, -8, 12])
b = Vector([2, 5, 4])

# Sum of Vector objects
sum = a + b
print(f"Adding vectors {a.val} and {b.val} is {sum.val}")

# Dot product of Vector objects
prod = a * b
print(f"Dot product of vectors {a.val} and {b.val} is {prod}")
