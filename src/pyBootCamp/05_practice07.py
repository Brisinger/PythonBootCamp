# Create a post from user
post = input("Post your details: ")
lookup = "Harry"
# Check if lookup text is present in post.
if (post.lower().startswith(lookup.lower()) or lookup.lower() in post.lower()):
    print(f"{post} is about {lookup} it's first occurence starts from index {post.lower().find(lookup.lower())}")
else:
    print(f"{post} is not about {lookup}")