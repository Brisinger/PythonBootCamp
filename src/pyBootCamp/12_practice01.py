try:
    with open("1.txt", "r") as f:
        f.read()
    with open("2.txt", "r") as f:
        f.read()
    with open("3.txt", "r") as f:
        f.read()
except FileNotFoundError as e:
    print(e)
except Exception as e:
    print(e)

print("Thanks for using this program.")