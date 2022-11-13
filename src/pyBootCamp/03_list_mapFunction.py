# Coverting iterator into list
x = ["ab", 'cd', 'xy']
# Output: [['a', 'b'], ['c', 'd'], ['x', 'y']]
print(list(map(list, x)))
# Iterator of characters
print(next(iter("ab")))
print(list("ab"))
print(x)
# Iterator of list
print(next(iter(x)))
print(list(x))
