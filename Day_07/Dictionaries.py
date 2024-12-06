# 1.Dictionaries are ordered collection of data items.
# 2.They store multiple items in a single variable. 
# 3.Dictionary items are key-value pairs that are separated by commas and enclosed within curly brackets {}.

student = {"name":"vivek","section":"K20GR"}
print(student)

# Accessing Dictionary items:
# I. Accessing single values:

# Values in a dictionary can be accessed using keys. We can access dictionary values by mentioning keys either in square brackets
# or by using get method.

print(student["name"])
print(student.get("section"))

print("-"*100)

# II. Accessing multiple values:
# We can print all the values in the dictionary using values() method.

print(student.values())

print("-"*100)

# III. Accessing keys:
# We can print all the keys in the dictionary using keys() method.

print(student.keys())
print("-"*100)

# IV. Accessing key-value pairs:
# We can print all the key-value pairs in the dictionary using items() method.

print(student.items())