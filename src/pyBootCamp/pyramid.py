n = 3
star = "*"
for i in range(0, n):
    print(" " * (n-i), end=" ")
    for j in range(0, i+1):
        print(star, end=" ")
    print()
for i in range(n-2, -1, -1):
    print(" " * (n-i), end=" ")
    for j in range(0, i+1):
        print(star, end=" ")
    print()
