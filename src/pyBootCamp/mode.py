"""Module to find the mode of Tuple input sequence in the order in which elements are inserted."""


my_tuple = tuple(eval(input("Enter the elements in a Tuple:")))

# Contains distinct elements from the Tuple input in the order of insertion.
my_list = []
max_freq = 0
mode_index = None

for item in my_tuple:
    if item not in my_list:
        my_list.append(item)

print(my_list)

# Initial values of frequency list will be 1, as an element must exist atleast once.
freq_list = [1] * len(my_list)

for i in range(0, len(my_list)):
    freq_list[i] = my_tuple.count(my_list[i])
    if freq_list[i] > max_freq:
        max_freq = freq_list[i]
        mode_index = i

print("Mode in sequence ", my_tuple, " is: ", my_list[mode_index])
