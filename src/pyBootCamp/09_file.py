f = open(file="09_this.txt", mode="r")
# Type of object returned by open function
print(type(f))
# Size of the file
print(f.__sizeof__())
txt = f.readline()
while (txt != ''):
    print(txt)
    txt = f.readline()
print(txt)
f.close()