# info = {"Carla", 19, False, 5.9, 19}
# print(info)

# Here we see that the items of set occur in random order and hence they cannot be accessed
# using index numbers. Also sets do not allow duplicate values.

# Quick Quiz: Try to create an empty set. Check using the type()
# function whether the type of your variable is a set

# vivek = set()
# print(type(vivek)) #empty set

# vivek1 = {}
# print(type(vivek1)) #empty dictionary

info = {"Carla", 19, False, 5.9}
for item in info:
    print(item)