from string import Template, capwords


# Defining template string
s = Template("$who likes $what")
print(s.substitute(who="Shubhojit", what="Python"))

# Defining dictionary mapping for substitution
d = {}
d.update(who="Shubhojit")
d.update(what="Python")
print(d)

# Defining template string with braces
print(Template("${who}'s book costs $price").substitute(d, price=100))
# Adding price key to dictionary
d.update(price=100)
# Placeholder mapping from keyword arguments take precedence
print(Template("${who}'s book costs $price").substitute(d, price=200))
# ValueError when placeholder following $ starts with non-identifier characters
try:
    print(Template("${who}'s book costs $price published by $").substitute(d, price=200))
except ValueError as e:
    print(e)
finally:
    print("Template contains another $ string.")
# KeyError when placeholder following $ is not provided as argument to substitute method
message = None
try:
    print(Template("${who}'s book costs $price published by $publisher").substitute(d, price=200))
except KeyError as e:
    message = e
    print(e)
finally:
    print(f"Placeholder for {message} doesn't have an associated key \
provided as argument to substitute method.")
# Concatenating template strings using join() method.
print("Template substitution using safe_substitute method")
msg = Template("${who}'s book costs $$$price published by $publisher").safe_substitute(d, price=200)
print(' and '.join([s.safe_substitute(d), msg]))
print(capwords(s.safe_substitute(d)), msg, sep=' and ')
