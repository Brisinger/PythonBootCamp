import os


# Define a function search for a word in a file
def search(path, lookup):
    # Opening file in read mode
    isFound = False
    with open(file=path, mode="r") as f:
        text = f.read().lower()
        isFound = (lookup.lower() in text) 
    return isFound

# Define a function to search and list text files containing a given word
# The lookup word is input from user
lookup = input("Enter the word: ")
# Define a function seaching files in a given path containing a word and listing them
searchPath = os.getcwd()

def searchFiles(path, lookup):
    # list containing files that have the input word as its content
    result = []
    # Fetching all the dir paths and file names with .txt extension in current working directory 
    for  dirPath, dirNames, fileNames in os.walk(path):
        for fileName in fileNames:
            if ('.txt' in os.path.splitext(fileName) and search(path=os.path.join(dirPath, fileName), lookup=lookup)):
                result.append(os.path.join(dirPath, fileName))
    return result

# Calling function to search files based on lookup and listing their paths
print(searchFiles(path=searchPath, lookup=lookup))
