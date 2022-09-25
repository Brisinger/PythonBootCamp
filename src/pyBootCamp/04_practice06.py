# Define empty dictionary
S = {}

# Fetch language preferences from 4 friends
S.update({input("Enter your Name: "): input("Your favorite language: ")})
S.update({input("Enter your Name: "): input("Your favorite language: ")})
S.update({input("Enter your Name: "): input("Your favorite language: ")})
S.update({input("Enter your Name: "): input("Your favorite language: ")})

# Display dictionary with friend's name as key and their language preference as value
print("\nPreferred language for 4 friends are:\n")
for friend, lang in S.items():
    print(f"{friend}'s preferred language is {lang} ")
