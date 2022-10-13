# Try-Except with finally block
try:
    a = int(input("Enter a number: "))
    b = int(input("Enter a number: "))
    print(f"{a}/{b}={a / b}")
    if (b>199):
        raise Exception(f"The number {b} is too large.")
except ValueError:
    print("Value error ocuured.")
except ZeroDivisionError:
    print("Cannot divide by", b)
except Exception as e:
    print(f"This problem ocuured: {e}")
else:
    print("Try executed successfully.")
finally:
    print("I will always be executed.")
