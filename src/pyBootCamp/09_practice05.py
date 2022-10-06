# Censored words
censored = {"donkey", "milk", "fuck", "breast"}
# File name
fileName = "09_practice05_file.txt"


# Define a function to censor list of words in text
def censorWords(text, *args) -> str:
    for word in args:
        word = word.lower()
        text = text.replace(word, "######")
        word = word.capitalize()
        text =text.replace(word, "######")
    return text


# Reading from file
with open(file=fileName, mode="r") as f:
    text = f.read()
    # Censoring words in list from text
    text = censorWords(text, *censored)

# Writing the censored text into file
with open(file=fileName, mode="w") as f:
    f.writelines(text)

