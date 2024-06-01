"""Module to print prime factors of a number from 1 till the number."""

n = int(input("Enter a positive integer: "))
if n <= 0:
    print("The entered number must be a positive integer.")

for i in range(1, n + 1):
    if i == 1:
        print(i, "=", i)
        continue
    print(i, "=", end=' ')
    k = i
    divisor = 2
    msg = ""
    symbol = "X"
    count = 0
    while k > 1:
        while k % divisor == 0:
            msg += str(divisor) + symbol
            k /= divisor
            count += 1
        divisor += 1
    else:
        msg = msg.rstrip(symbol)
    if count == 1:
        print(msg, "(prime)")
    else:
        print(msg)
