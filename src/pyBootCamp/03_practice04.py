listOfNumbers = []
number = int(input("Enter the 1st Number: "))
listOfNumbers.append(number)
number = int(input("Enter the 2nd Number: "))
listOfNumbers.append(number)
number = int(input("Enter the 3rd Number: "))
listOfNumbers.append(number)
number = int(input("Enter the 4th Number: "))
listOfNumbers.append(number)

sum = 0
sum += listOfNumbers[0]
sum += listOfNumbers[1]
sum += listOfNumbers[2]
sum += listOfNumbers[3]

print("The sum of", len(listOfNumbers), "numbers in list", listOfNumbers, "is:", sum)

