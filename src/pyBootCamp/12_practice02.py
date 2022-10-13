listOfNumbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# Display the 3rd, 5th nd 7th elements
for index, item in enumerate(listOfNumbers):
    if (index + 1 == 3) or (index + 1 == 5) or (index + 1 == 7):
        print(item)