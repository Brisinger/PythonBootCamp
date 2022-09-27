# Enter the number from input
number = int(input("Enter the number: "))

for num in range(1, number + 1):
    spaces = number - num
    stars = (2*num) - 1
    print(f"{' '*spaces}{'*'*stars}{' '*spaces}")


