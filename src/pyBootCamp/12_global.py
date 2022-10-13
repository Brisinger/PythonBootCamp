# a = 9
# Defining a function with global variable
def wrapper(a):
    # Displaying the value of a before modification
    print("Value of a before calling the function func", a)   
    def func():
        global a
        a = int(input("Enter a number: "))
        print("Value of a in function scope", a)
    func()

# Calling function
wrapper(9)

# Displaying the value of a before modification
print("Value of a outside function scope before calling the function", a)

# Displaying the value of a outside function
print("Value of a outside function scope after function call", a)