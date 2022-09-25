myNumber = 1
oxford = {
    "gift": "Something willingly given to someone to appreciate",
    "linq": "A feature in C# for querying collections and iterables",
    "Youtube": "A video sharing platform",
    "Instagram": "A picture sharing platform",
    "myListOfNumbers": [1,8,7,2,21,15],
    myNumber: "one"
}
# list of key, value pairs
print("\nList of key, value pairs in dictionary", oxford)

for a, b in oxford.items():
    print(f"key: {a}, value: {b}")

# Display the keys of dictionary
print("\nList of keys in dictionary:", oxford.keys())
print("\nType of keys list is:", type(oxford.keys()))
print("\nList the keys in dictionary", oxford, "are as follows:\n")
print("[", end='')
for key in oxford.keys():
    print(f"{key}", end=', ') if oxford[key] is not 'one' \
    else print(f"{key}", end=']')

#  Adding key, value pairs and updating existing key, value pairs.
print("\nAdding key, value pairs", {("Shubhojit", "Good boy!"), ("myList", "[56, 8]")}, "into dictionary.")
oxford.update({"Shubhojit": "Good boy!", "myList": [56, 8]})
print("\nUpdated dictionary:", oxford)

# Get the values of dictionary keys.
print("\nList the values of dictionary keys")
print("\n{0}: {1}".format('linq', oxford['linq']))
try:
    print("\n{0}: {1}".format('not', oxford['not']))
except KeyError as e:
    print("\n{0} of the keys in dictionary matches {1}".format(oxford.get('not'), e))

