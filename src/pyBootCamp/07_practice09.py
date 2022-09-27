# Enter the number from input
number = int(input("Enter the number: "))

for num in range(1, number + 1):
    spaces = number - 2 if (num>1) and (num<number) else 0 
    stars = number if (num==1) or (num==number) else 1
    if not(spaces):
        print(f"{'*'*number}")
    else:
        print(f"*{' '*spaces}*")