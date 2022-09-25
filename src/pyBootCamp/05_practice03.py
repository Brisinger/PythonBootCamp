# Define a set of spams
spamSet = {"make a lot of money", "buy now", "subscribe this", "click this"}
# Getting comment from user
comment = input("Enter your comment: ").lower().replace(' ', '')
isSpam = False
# Detecting spam in comment
for item in spamSet:
    if (item.lower().replace(' ', '') in comment):
        isSpam = True
        print(f"Spam {item} detected")

if not isSpam:
    print(f"comment: {comment} is posted")
