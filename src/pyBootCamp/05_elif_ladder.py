# if-elif ladder
print("if-elif ladder using elif keyword in python\n")
age = int(input("Enter your Age: "))
if age>4 and age<=14:
    print("Go to school")
elif (age>14) & (age <16):
    print("Go to high school")
elif age >= 16 and age<18:
    print("Join to internship")
elif age>18:
    print("Go to driving school")
else:
    print("Enjoy")