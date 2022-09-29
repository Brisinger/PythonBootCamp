# Define a function to remove a word after stripping trailling whitespaces from a list
def process(listOfWords, word):
    isRemoved = False
    word = word.strip()
    if (word in listOfWords):
        isRemoved = True
        listOfWords.remove(word)
    return isRemoved

listOfWords = ["Harry", "Roshan", "Shubham", "Shubhojit"]
# Input the word to remove from user
print(f"List of words: {listOfWords}")
word = input("Enter the word to be removed from list: ")
isRemoved = process(listOfWords=listOfWords, word=word)

# Check if word is removed
if isRemoved:
    print(f"\n({word}) removed from list")
    print(f"List after removal: {listOfWords}")
else:
    print(f"\nFailed to remove ({word})")
    print("\n({0}) not found in {1}".format(word, listOfWords))
