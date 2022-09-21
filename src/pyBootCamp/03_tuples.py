myTuple = (3, 6, 7)
print(myTuple)
print(type(myTuple))
# myTuple[0] = 4 --> TypeError: 'tuple' object does not support item assignment as it is immutable.

# Empty tuple
print("Empty tuple: {0} and it's type is {1} ".format((), type(())))

# Single element tuple
# This will not be a tuple but integer
print("\n(4) will not be a tuple but integer.") 
print("Singleton tuple without comma: {0} and it's type is {1} ".format((4), type((4))))
print("\n(4,) is a tuple and not an integer.") 
print("Singleton tuple with comma: {0} and it's type is {1} ".format((4,), type((4,))))
