# Conversion to centimeters dictionary
CONVERTION_TO_CENTIMETER = {
    'inch': 2.54,
    'feet': 30.48
}
# Define function to convert inches to centimeters
def toCentimeter(inches):
    return CONVERTION_TO_CENTIMETER['inch'] * inches
# Get length as input from user
inches = float(input("Enter length in inches: "))
# Display length in centimeters upto 4 decimals float precision
print(f"Length {inches} in to centimeters is {toCentimeter(inches=inches):0.4f} cm")