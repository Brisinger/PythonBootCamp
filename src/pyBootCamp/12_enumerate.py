# Defining a list of items
a = [1, 4, 6, 'apple']
# Create an iterator
e = enumerate(a, start=1)
print("Type of iterator", type(e))
item = next(e)
while True:
    print(item)
    try:
        item = next(e)
    except StopIteration as ex:
        print("Iterable Traversed till end.")
        break
print("Enumerated Successfully.")
    