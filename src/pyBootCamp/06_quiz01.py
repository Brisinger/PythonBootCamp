# Print numbers from 1 to 50 using while loop
counter = 1
while (counter<=50):
    print(counter, end=", ") if counter<50 else print(counter, end='')
    counter += 1
else:
    print("\nWhile loop exited successfully\n")