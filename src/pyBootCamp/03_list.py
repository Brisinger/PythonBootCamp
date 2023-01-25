a = 12
b = "This is a string"
c = False

myList = [a, b, c]
print(myList)
print(type(myList))
# print(myList[4]) raises IndexError
# Sequence unpacking.
x, y, _ = myList
print(x, y, _)