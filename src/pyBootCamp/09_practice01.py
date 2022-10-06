# Defining a function to lookup a text in given file
def search(file, lookup):
    # Opening file in read mode
    isFound = False
    with open(file=file, mode="r") as f:
        poem = f.read().lower()
        isFound = (lookup.lower() in poem) 
    return isFound

# Input search text from user
lookup = input("Enter the search text: ")

# Searching file 09_poem.txt for the lookup text
if (search("09_poem.txt", lookup)):
    print(f"{lookup} found in 09_poem.txt")
else:
    print(f"{lookup} not found in 09_poem.txt")
            

