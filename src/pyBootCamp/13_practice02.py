with open(file="12_practice05.txt", mode="r") as f:
    myList = f.read().rstrip(']').lstrip('[').split(', ')
    str = '\n'.join(myList)
    print(str)
    