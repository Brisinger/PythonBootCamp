# Function to convert temperature from celsius to farenheit
def celtofar(cel):
    return (cel * 9/5) + 32
# Input celsius value
celsius = float(input("Enter temperature in celsius: "))
# Display temperature in farenheit by invoking celtofar
print("Temperature in farenheit is:", celtofar(celsius))