myStr = "abcdefghijklmnopqrstuvwxyz0123456789"

# Find length of the string
print("Length of string")
print(len(myStr))

# Checks if string ends with given set of characters or string eg. "789"
print("\nString endswith")
print(myStr.endswith("789"))
print(type(myStr.endswith("789")))
print(myStr[1:19])
print(myStr.endswith(("mnopq", "pqrs"), 1, 19))

# Checks if string ends with given set of characters or string eg. "abc"
print("\nString startwith")
print(myStr.startswith("abc"))
print(myStr.startswith(("mnopq", "pqrs", "bcd"), 1, 19))

# Count occurence of given character in a string
print("\nCount occurences of character")
name = "Shubhojit dasgupta"
# Count No. of occurence of a character in given string.
print("'t' occurs", name.count('t'), "times in", name)
print("'th' occurs", name.count('th'), "times in", name)

# First character uppercased
print("\nCapitalized version of", name, "is", name.capitalize())

# The start of each word is uppercased
print(f"\n{name} is titlecased to", name.title())

# Finding starting index of the first occurence of a word in given string
name = "My name is Shubhojit"
print("First occurence of Shubho:", name.find("Shubho"))
name = name.replace("Shubhojit", "Shubho")
print(name)
