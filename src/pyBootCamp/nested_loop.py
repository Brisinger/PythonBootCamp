"""
*
* *
* * *
* * * *
"""
n = 1
k = 6
step = 1
count = 2

while count > 0:
    for i in range(n, k, step):
        for j in range(1, i):
            print("*", end=' ')
        print()
    count = count - 1
    if count > 0:
        n = 4
        k = 1
        step = -1
