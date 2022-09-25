# Defining a set variable by initialisation
print("Defining a set by initialisation")
S = {1, 8, 3, 2}
# Displaying the values of set
print("\nThe {0} contains {1}".format(type(S).__name__, S))

# Defining an empty set
empty = set()
print("\nType of empty variable is {0} with value {1}".format(type(empty), empty))

# Type of {}
print("\nType of {} is", type({}), "not", type({None}))

# Empty set initialized with None element type
empty = {None}
print("\nType of empty variable is {0} with value {1}".format(type(empty), empty))

# Empty set initialized with empty string element type
empty = {''}
print("\nType of empty variable is {0} with value {1}".format(type(empty), empty))

# Find the length of set
print("\nLength of the", type(S).__name__, "is", len(S))

# Adding elements to set and displaying it's length
print("\nAdd duplicate element 1 to set")
S.add(1)
print("\nLength of the", type(S).__name__, "is", len(S))

print("\nAdd duplicate element 2 to set")
S.add(2)
print("\nLength of the", type(S).__name__, "is", len(S))

print("\nAdd nothing to set with no parameter specified")

try:
    S.add()
except TypeError as e:
    print(f"{e} must take exactly one argument")

print("\nLength of the", type(S).__name__, "is", len(S))

print("\nAdd element '1' to set")
S.add("1")
print("\nLength of the", type(S).__name__, "is", len(S))

# Removing elements from a set
print("\nElements in set:", S)
print("\nRemove element '1' from set")
S.remove('1')
print("\nElements in set after removing '1' are:", S)
print("\nRemove element '1' from set")

try:
    S.remove('1')
except KeyError as e:
    print(f"\n{e} does not exist in set", S)

print("\nLength of the", type(S).__name__, "is", len(S))

# Removing an element randomly and returning it
print("\nElements in set:", S)
print("\nRemove random element from set")
element = S.pop()
print("\nElements in set after removing", element, S)
print("\nLength of the", type(S).__name__, "is", len(S))

# Union set operation
print("\nUnion set operation")
S1 = {8, 11}
print(f"\n{S} U {S1} = {S.union(S1)}")

# Intersection set operation
print("\nIntersection set operation")
S1 = {8, 11}
print(f"\nIntersection of {S} and {S1} = {S.intersection(S1)}")

# Clear set operation results in empty set
print("\nClear all the elements of set")
S.clear()
print(f"\nType of variable S is", type(S), "with value", S)
print("\nLength of the", type(S).__name__, "is", len(S))

