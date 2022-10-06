import os


# Define mulyiplication table in function
def multiply(mul, start=1, stop=12):
    # Current working directory
    path = os.getcwd()
    folder = "09_multiplication"
    # Check if path does not exist
    if (not os.path.exists(os.path.join(path, folder))):
        # Create the folder 
        os.mkdir(path=os.path.join(path, folder))
    # File name for storing multiplication table of number
    fileName = f"09_multiplication_of_{mul}.txt"
    # Writing the multiplication table into file
    with open(os.path.join(path, folder, fileName), mode='w') as fp:
        for num in range(start, stop + 1):
            text = f"{mul} X {num} = {mul * num}"
            fp.write(text)
            fp.write("\n")
    # Displaying the file path where multiplication table is stored
    print(f"\nMutiplcation table of {mul} created in path: {os.path.join(path, folder, fileName)}\n")

# Input the starting number as multiplicand from user
first = int(input("Enter the starting range Number as multiplicand for multiplication: "))
# Input the starting number as multiplier from user
start = int(input("Enter the start multiplier of multiplication: "))
# Input the ending number as multiplier from user
end = int(input("Enter the end multiplier of multiplication: "))
# Input the last number as multiplicand from user
last = int(input("Enter the ending range Number as multiplicand for multiplication table: "))

print(f"\nCreating multiplication tables from {first} to {last}")
for i in range(first, last+ 1):
    multiply(mul=i, start=start, stop=end)