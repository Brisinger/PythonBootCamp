# Defining map, filter and reduce functions
from functools import reduce


input_list = [7, 14, 21, 28, 35, 42, 49, 56, 63, 70, 77, 84]
# Creating a map object
print("Creating map object")
result = map(lambda x: divmod(x, 2), input_list)
print(type(result))
# Creating a generator object
result = ((x, y) for x, y in result if y == 0)
print("Creating generator object")
print(type(result))
print(next(result))
print(tuple(result))
# Demonstration of filter function
print("Creating filter object")
result = filter(lambda x: x % 2 == 1, input_list)
print(type(result))
print(list(result))
print("This is my string.".split())
print("Creating filter object without function")
a = [1, 2, "and", "", None]
result = filter(None, a)
print(list(result))
# Demonstration of reduce function
print("Demonstration of reduce function on iterables")
myList = [1, 2, 7, 3]
result = reduce(lambda x, y: x + y, myList)
print(type(result))
print(result)
print(reduce(max, myList))


