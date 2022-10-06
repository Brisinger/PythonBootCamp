# Open a file using with keyword context manager in write mode
with open(file="09_this.txt", mode="w") as f:
    f.write("Python file management is very simple.\n")
    f.write("Python opens a file using open() function.\n")
    f.write("If an object has context manager defined it can be used in with statement. When it exists it closes the file automatically.")