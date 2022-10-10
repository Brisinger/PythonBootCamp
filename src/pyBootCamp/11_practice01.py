# Defining classes for Vectors
"""
Class representing 2-D Vectors
"""
class Vector2d:
    def __init__(self, i, j) -> None:
        self.i = i
        self.j = j
    
    def displayVector(self):
        print(f"{self.i}i + {self.j}j")

"""
Class extending 2-D Vectors to 3-D Vectors
"""
class Vector3d(Vector2d):
    def __init__(self, i, j, k) -> None:
        self.k = k
        super().__init__(i, j)
    
    def displayVector(self):
        print(f"{self.i}i + {self.j}j + {self.k}k")

# Creating object for 2D vector
v2 = Vector2d(1, 5)
# Creating object for 3D vector
v3 = Vector3d(1, 5, 9)

# Displaying vectors
print("Display", v2.__class__.__qualname__, ":")
v2.displayVector()
print("Display", v3.__class__.__qualname__, ":")
v3.displayVector()
