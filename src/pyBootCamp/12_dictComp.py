dictOfFruits = {"Apple": 12, "Orange":2 , "Mango": 6, "Pomegranate": 4} 
print(dictOfFruits)
# Defining dict comprehension
dictOfNumbers = { num:fruit for fruit, num in dictOfFruits.items()}
print(dictOfNumbers)