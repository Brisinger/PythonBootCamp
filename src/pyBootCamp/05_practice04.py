# Get username as input
username = input("Enter your User Name: ")

# Detect if length of username is less than 10 characters long
if (len(username) < 10):
    print(f"Enter username with 10 or more characters long.")
else:
    print(f"Hello, {username}")
