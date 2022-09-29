# Defining a function
def func():
    print("function")
    return "fn()"
# Invoking function
func()
# Greeting user
def greet(name="Shubhojit Dasgupta"):
    return "Hello, " + name 
# Greeting with user
greetings = greet("Harry")
print(f"{greetings}")
# Greeting without user
greetings = greet()
print(f"{greetings}")