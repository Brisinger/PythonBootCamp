import os


# Input from user for file to rename
oldName = input("Enter the name of file to rename: ")
newName = input("Enter the new name of the file: ")

# Define a function to rename an existing file
def rename(oldFile, newFile):
    os.rename(oldFile, newFile)

# Renaming the file
print("Renaming file", oldName, "to", newName)
rename(oldName, newName)
