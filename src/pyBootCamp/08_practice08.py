import os


# Define mulyiplication table in function
def multiply(mul, start=1, stop=12):
    # Current working directory
    path = os.getcwd()
    # File name for storing multiplication table of number
    fileName = f"08_multiplication_of_{mul}.txt"
    # Writing the multiplication table into file
    with open(os.path.join(path, fileName), mode='w') as fp:
        for num in range(start, stop + 1):
            text = f"{mul} X {num} = {mul * num}"
            fp.write(text)
            fp.write("\n")
    # Displaying the file path where multiplication table is stored
    print(f"\nMutiplcation table of {mul} created in path: {os.path.join(path, fileName)}\n")
# Input the number from user
number = int(input("Enter the Number for multiplication: "))
start = int(input("Enter the start of multiplication: "))
end = int(input("Enter the end of multiplication: "))
# Create multiplcation table for input
print("Creating multiplication table of", number)
# Invoking function to create mutiplication table
multiply(number, start=start, stop=end)