"""Module to convert integers between 0-3999 from user's input into equivalent Roman Numerals.
  Stores the Roman Numeral as a string.
"""

# Integer provided by user.
number = int(input("Enter a number from 0 to 3999: "))

# Dictionary mapping an integer to equivalent Roman Numeral as a string.
roman = {
    1000: "M",
    900: "CM",
    500: "D",
    400: "CD",
    100: "C",
    90: "XC",
    50: "L",
    40: "XL",
    10: "X",
    9: "IX",
    5: "V",
    4: "IV",
    1: "I"
}

if number > 3999:
    print("Unable to convert to equivalent Roman Numeral as",
          number, "is greater than 3999")
elif number < 0:
    print("You have entered a negative integer:", number)
    print("Negative Integers cannot be converted to equivalent Roman Numerals.")
else:
    result = ""
    unit = 1  # One's place initially.
    while number:
        """Gather successive digits in the number from right to left.
          Modulo operator evaluates to a float type. 
          Convert the value of the operation to int type before storing it in variabe digit.
          The variable digit is used in integer division with is not compatible with float types.
        """
        digit = int(number % 10) * unit
        if digit == 0:
            # Unit placeholder one's, ten's, hundered's and thousand's place in an integer.
            unit *= 10
            number /= 10
            continue
        elif digit > 0 and digit < 4:
            result = roman[1] * digit + result
        elif digit == 4:
            result = roman[digit] + result
        elif digit >= 5 and digit < 9:
            result = roman[5] + roman[1] * (digit - 5) + result
        elif digit == 9:
            result = roman[digit] + result
        elif digit >= 10 and digit < 40:
            result = roman[10] * (digit // unit) + result
        elif digit == 40:
            result = roman[digit] + result
        elif digit >= 50 and digit < 90:
            result = roman[50] + roman[10] * ((digit - 50) // unit) + result
        elif digit == 90:
            result = roman[digit] + result
        elif digit >= 100 and digit < 400:
            result = roman[100] * (digit // unit) * result
        elif digit == 400:
            result = roman[digit] + result
        elif digit >= 500 and digit < 900:
            result = roman[500] + roman[100] * ((digit - 500) // unit) + result
        elif digit == 900:
            result = roman[digit] + result
        else:
            result = roman[1000] * (digit // unit) + result
        # Multiply the placeholder by 10 to represent the next digit in the number.
        unit *= 10
        # remove the digits from the number from right to left.
        number /= 10
    print(result)
