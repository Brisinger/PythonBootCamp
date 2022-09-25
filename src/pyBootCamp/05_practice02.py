mark1 = int(input("Enter the marks for sub 1: "))
mark2 = int(input("Enter the marks for sub 2: "))
mark3 = int(input("Enter the marks for sub 3: "))

average = (mark1 + mark2 + mark3)/3
# Overall percent should be greater or equal to 40 and pass mark in each subject is 33
if (average>=40):
    if (mark1<33):
        print("You have failed the exam for sub 1")
    if (mark2<33):
        print("You have failed the exam for sub 2")
    if (mark3<33):
        print("You have failed the exam for sub 3")
    if(mark1>=33)&(mark2>=33)&(mark3>=33):
        print("You have passed the exam")
else:
    print("You have failed the exam due to overall average being less than 40")
    if (mark1<33):
        print("You have failed the exam for sub 1")
    if (mark2<33):
        print("You have failed the exam for sub 2")
    if (mark3<33):
        print("You have failed the exam for sub 3")