import os


# Clear contents of file using truncate function
def clear(file):
    with open(file=file, mode="a") as f:
        print(f"Resizing {file} to {f.truncate(0)} bytes.")

# Clear contents of file by writing an empty content
def clearByWritingEmptyContent(file):
    with open(file=file, mode="w") as writer:
        print(writer.write(''))

# file name in current path
file = "09_sample1.txt" 

# Removing contents of file
print("Size of", file, "in bytes before removing it's content is", os.path.getsize(file))
clear(file=file)
print("Size of", file, "in bytes after removing it's content is", os.path.getsize(file))

# Removing contents of file by writing empty content
print("Size of", file, "in bytes before removing it's content is", os.path.getsize(file))
clearByWritingEmptyContent(file=file)
print("Size of", file, "in bytes after removing it's content is", os.path.getsize(file))


