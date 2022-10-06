# Reading the file
with open(file="09_practice04_file.txt", mode="r") as f:
    text = f.read()

# Replace donkey text with ######
text = text.replace("donkey", "######")
text = text.replace("Donkey", "######")

# Writing to the file the updated text
with open(file="09_practice04_file.txt", mode="w") as f:
    f.write(text)
