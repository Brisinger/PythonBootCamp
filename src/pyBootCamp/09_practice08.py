# Copying contents of one file to another file
with (
    open(file="09_this.txt", mode="r") as reader,
    open(file="09_thiscopy.txt", mode="w") as writer):
    text = reader.readlines()
    writer.writelines(text)
