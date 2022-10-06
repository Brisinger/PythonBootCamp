# Opening the file
f = open(file="09_this.txt", mode="r+")
# Type of object
print(type(f))
text = f.readlines()
print(f"Type of text returned by readline() method is {type(text)}", text)
print("\nContent of file '09_this.txt':\n")
for txt in text:
    print(txt)

