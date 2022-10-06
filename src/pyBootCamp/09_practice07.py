import os


# Define function for listing all line numbers in text files of current directory where given word is present
def search(file, lookup) -> dict:
    lineNumbers = []
    result = {}
    if ('.txt' in os.path.splitext(file)):
        with open(file=file, mode="r") as reader:
            lineNo = 0;
            for line in reader:
                lineNo += 1
                line = line.lower()
                lookup = lookup.lower()
                if (lookup in line):
                    lineNumbers.append(lineNo)
                    result.update({file: lineNumbers})
        return result
    else:
        return result
# Second way of searching file line by line
def search2(file, lookup) -> dict:
    lineNumbers = []
    result = {}
    if ('.txt' in os.path.splitext(file)):
        with open(file=file, mode="r") as reader:
            lineNo = 0;
            for line in reader.readlines():
                lineNo += 1
                line = line.lower()
                lookup = lookup.lower()
                if (lookup in line):
                    lineNumbers.append(lineNo)
                    result.update({file: lineNumbers})
        return result
    else:
        return result


# Third way of searching file line by line
def search3(file, lookup) -> dict:
    lineNumbers = []
    result = {}
    if ('.txt' in os.path.splitext(file)):
        with open(file=file, mode="r") as reader:
            lineNo = 0;
            line = reader.readline()
            while line != '':
                lineNo += 1
                line = line.lower()
                lookup = lookup.lower()
                if (lookup in line):
                    lineNumbers.append(lineNo)
                    result.update({file: lineNumbers})
                else:
                    result.update({file: lineNumbers})
                line = reader.readline()
        return result
    else:
        return result


# Input lookup from user to search in current directory
lookup = input("Enter the search keyword: ")
# Searching text files in current directory returning a dictionary containing file as key
# The line numbers in file containing lookup is the value associated with key
def searchFiles(lookup):
    results = {}
    for file in os.listdir():
        # returning file and its line numbers containing the lookup word
        results.update(search(file=file, lookup=lookup))
    return results
print("\nSearching files in current directory:", os.getcwd())
# Listing files and line numbers as dictionary key value pairs
result = searchFiles(lookup)
print(result)

# Searching text files in current directory returning a dictionary containing file as key
# The line numbers in file containing lookup is the value associated with key
def searchFiles2(lookup):
    results = {}
    for file in os.listdir():
        # returning file and its line numbers containing the lookup word
        results.update(search2(file=file, lookup=lookup))
    return results
print("\nSearching files in current directory:", os.getcwd())
# Listing files and line numbers as dictionary key value pairs
result = searchFiles2(lookup)
print(result)

# Searching text files in current directory returning a dictionary containing file as key
# The line numbers in file containing lookup is the value associated with key
def searchFiles3(lookup):
    results = {}
    for file in os.listdir():
        # returning file and its line numbers containing the lookup word
        results.update(search3(file=file, lookup=lookup))
    return results
print("\nSearching files in current directory:", os.getcwd())
# Listing files and line numbers as dictionary key value pairs
result = searchFiles3(lookup)
print(result)