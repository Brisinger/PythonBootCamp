# Defining a list of numbers
myListOfNumbers = [1,8,7,2,21,15]
print(myListOfNumbers)

# Sorting the list
print("\nSorting the list:", myListOfNumbers, "in ascending order.")
#print(myListOfNumbers.sort()) --> returns None
myListOfNumbers.sort()

# Printing the contents of list using for loop without modifying the list
print("\nDisplaying the list", myListOfNumbers, "using for loop")
counter = 0
for item in myListOfNumbers:
    print(item, end=", ") if counter<(len(myListOfNumbers) - 1) else \
    print(item)
    counter += 1
else:
    print(f"\nList displayed with {counter} elements in for loop successfully\n")