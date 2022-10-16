from functools import reduce


# Find max in list of numbers with reduce function
my_numbers = [-2, -1, 1, 0]
print(reduce(max, my_numbers))