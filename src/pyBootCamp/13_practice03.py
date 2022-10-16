# using filter function
my_numbers = [2, 4, 5, 6, 10, 15, 20, 25, 11, 12]
result = filter(lambda x: x % 5 == 0, my_numbers)
print(list(result))