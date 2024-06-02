rows = 5
for i in range(1, rows + 1):
    # Print spaces for alignment
    print(" " * (rows - i), end="")

    # Print numbers in increasing order
    for j in range(i, 0, -1):
        print(j, end="")

    # Print numbers in decreasing order
    for j in range(2, i + 1):
        print(j, end="")

    # Move to the next line after printing each row
    print()
