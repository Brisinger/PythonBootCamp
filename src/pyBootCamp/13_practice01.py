from string import Template


# Input for the student
d = {}
d.update(name = input("Enter student name: "))
d.update(marks = float(input("Enter the marks: ")))
d.update(phone = input("Enter student's Phone Number: ") )

# Define a template string
template = Template("The name of the student is $name, his marks are $marks and phone number is $phone")
# Display the string by substitution of placeholders with dictionary mapping
marks = "%.2f" %(d.get("marks"))
print(template.safe_substitute(d, marks=marks))