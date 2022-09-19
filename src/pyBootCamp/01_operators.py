a = 7
b = 3

# Arithmetic operators
print("Demonstrating Arithmetic Operators in Python")

print("a + b = ", a + b)
print("a - b = ", a - b)
print("a * b = ", a * b)
print("a / b = ", a / b)

# Assignment operators
print("\nDemonstrating Assignment Operators in Python")
c = 5
d = 7
print(c, d)

c += 5
d += 1
print(c, d)

c -= 5
d -= c
print(c, d)

# Comparison operators
print("\nDemonstrating Comparison Operators in Python")
e = 6
f = 6
print(e == f)
print(e > f)
print(e < f)
# Checks for equality in value and data type
print(e is f)
print(e is not f)
print(e != f)

f = 6.0
print("\n")
print(e == f)
print(e > f)
print(e < f)
print(e is f)
print(e is not f)
print(e != f)

e = 6.001
f = 6.0
print("\n")
print(e == f)
print(e > f)
print(e < f)
print(e is f)
print(e is not f)
print(e != f)

# Logical operators
print("\nDemonstrating Logical Operators in Python")
e = 6
f = 9
print(e==f and e>f)
print(e==f or e<f)
print(not(e>f))
