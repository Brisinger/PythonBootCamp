myListOfNumbers = [1,8,7,2,21,15]
print(myListOfNumbers)

# Sorting the list
print("\nSorting the list:", myListOfNumbers, "in ascending order.")
#print(myListOfNumbers.sort()) --> returns None
myListOfNumbers.sort()
print(myListOfNumbers)
print("\nSorting the list:", myListOfNumbers, "in descending order.")
myListOfNumbers.sort(reverse=True)
print(myListOfNumbers)

# Reverses original list
print("\nReversing the list:", myListOfNumbers)
myListOfNumbers.reverse()
print(myListOfNumbers)

# Adding a value to the end of the list
print("\nAdd 9 at the end of the list:", myListOfNumbers)
myListOfNumbers.append(9)
print(myListOfNumbers)
# Inserting an element at a particular index of list
print("\nInserts 9 at index 2 of the list:", myListOfNumbers)
myListOfNumbers.insert(2, 9)
print(myListOfNumbers)

# Deleting an element from a particular index of list
print("\nDeleting the last element of the list:", myListOfNumbers)
myListOfNumbers.pop()
print(myListOfNumbers)
print("\nDeleting the element at index 2 of the list:", myListOfNumbers)
myListOfNumbers.pop(2)
print(myListOfNumbers)

# Remove an element from a list by specifying the element only and not index
print("\nDeleting the element", myListOfNumbers[-1], "from the list:", myListOfNumbers)
myListOfNumbers.remove(21)
print(myListOfNumbers)

# Removing duplicate elements from the list.
myListOfNumbers.append(7)
print("\nList before removing duplicate element 7:", myListOfNumbers)
myListOfNumbers.remove(7)
print("\nAfter removing duplicate element 7 from the list :", myListOfNumbers)
print("\nInsert 2 at index 4 of the list:", myListOfNumbers)
myListOfNumbers.insert(4, 2)
print("\nInserts 15 at index 1 of the list:", myListOfNumbers)
myListOfNumbers.insert(1, 15)
print(myListOfNumbers)
myListOfDistinctNumbers = []
resultList = []
for num in myListOfNumbers:
    if num not in resultList:
        myListOfDistinctNumbers.append(num)
    resultList.append(num)    
print(resultList)
print("\nRemoving all duplicates from list:", myListOfDistinctNumbers)





