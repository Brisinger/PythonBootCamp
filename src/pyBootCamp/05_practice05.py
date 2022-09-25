# Defining a whitelist of names
whitelist = ["Abhishiek", "Shubhojit", "Harry"]
# Entered name by user
name = input("Enter your Name: ")
# Check if user is allowed access
if (name in whitelist):
    print(f"{name} is allowed access")
else:
    print(f"{name} is denied access")
