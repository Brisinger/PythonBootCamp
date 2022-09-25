# Defining a set data type
mySet = set()
print("Type of mySet variable is", type(mySet))
# Adding elements to a set.
print("\nAdding 1 to set")
mySet.add(1)
print("\nSet after adding element 1:", mySet)
print("\nAdding 2 to set")
mySet.add(2)
print("\nSet after adding element 2:", mySet)
print("\nAdding duplicate element 2 to set")
mySet.add(2)
print("\nSet after adding element 2 twice:", mySet)

# Iterating items in a set
print("\nListing elements of set", mySet)
print(end="{")
count = 0
for item in mySet:
    count += 1
    print(item, end=', ') if count is not len(mySet) else  print(item, end='') 
print(end="}")

# Adding a list variable to set
myListOfNumbers = [1,8,7,2,21,15]
print("\nAdding list to set:", myListOfNumbers)
try:
    mySet.add(myListOfNumbers)
except TypeError as e:
    print(f"Cannot add {e} {myListOfNumbers} to set", mySet)
print("\nSet after adding list:", mySet)

