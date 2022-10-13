# Try-Except block prevents code from halting by handling exceptions
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
print("There are no errors.")