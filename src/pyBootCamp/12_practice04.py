# Define a function to display fraction
def fraction(a, b):
    try:
        if isinstance(a, int) and isinstance(b, int):
            if (b!=0):
                return ("%s" %(a) + "/" + "%s" %(b))
            else:
                raise ZeroDivisionError("Infinite")
        else:
            raise ValueError("Undefined")
    except ZeroDivisionError as e:
        return e
    except ValueError as e:
        return e

# Input from user
numerator = int(input("Enter the Numerator: "))
denominator = int(input("Enter the Denominator: "))
print(fraction(numerator, denominator))