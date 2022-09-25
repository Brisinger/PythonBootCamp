oxford = {
    "lakdi": "wood",
    "kursi": "chair",
    "chaku": "knife"
}
key = input("Enter the key\n")
if oxford.get(key):
    print(f"The value corresponding to {key} is {oxford[key]}")
else:
    print(f"{key} not found in dictionary")