marks = []
mark = input("Enter the marks of the 1st student: ")
marks.append(float(mark))
mark = input("Enter the marks of the 2nd student: ")
marks.append(float(mark))
mark = input("Enter the marks of the 3rd student: ")
marks.append(float(mark))
mark = input("Enter the marks of the 4th student: ")
marks.append(float(mark))
mark = input("Enter the marks of the 5th student: ")
marks.append(float(mark))
mark = input("Enter the marks of the 6th student: ")
marks.append(float(mark))

print("\nSorting the marks of 6 students in ascending order")
marks.sort()
print("\nMarks of 6 students in sorted order:", marks)