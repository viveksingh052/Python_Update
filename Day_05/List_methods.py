#List Methods

# 1.sort()
# This method sorts the list in ascending order. The original list is updated
# colors = ["voilet", "indigo", "blue", "green"]
# colors.sort()
# print(colors)

# num = [4,2,5,3,6,1,2,1,2,8,9,7]
# num.sort()
# print(num)

# What if you want to print the list in descending order?.
# We must give reverse=True as a parameter in the sort method.

# colors = ["voilet", "indigo", "blue", "green"]
# colors.sort(reverse=True)
# print(colors)

# num = [4,2,5,3,6,1,2,1,2,8,9,7]
# num.sort(reverse=True)
# print(num)

# 2.reverse()
# This method reverses the order of the list.

# colors = ["voilet", "indigo", "blue", "green"]
# colors.reverse()
# print(colors)

# num = [4,2,5,3,6,1,2,1,2,8,9,7]
# num.reverse()
# print(num)

# 3.index()
# This method returns the index of the first occurrence of the list item.

# colors = ["voilet", "green", "indigo", "blue", "green"]
# print(colors.index("green"))

# num = [4,2,5,3,6,1,2,1,3,2,8,9,7]
# print(num.index(7))


# 4.count()
# Returns the count of the number of items with the given value.

# colors = ["voilet", "green", "indigo", "blue", "green"]
# print(colors.count("green"))

# num = [4,2,5,3,6,1,2,1,3,2,8,9,7]
# print(num.count(1))

# 5.copy() 
# Returns copy of the list. This can be done to perform operations
# on the list without modifying the original list.

# colors = ["voilet", "green", "indigo", "blue"]
# newlist = colors.copy()
# print("This is the colors list",colors)
# print("This is the newlist",newlist)

# 6.append():
# This method appends items to the end of the existing list.

# colors = ["voilet", "indigo", "blue"]

# colors.append("maroon")
# print(colors)

# 7.insert():
# This method inserts an item at the given index. User has to specify index
# and the item to be inserted within the insert() method.

# colors = ["voilet", "indigo", "blue"]

# colors.insert(2,"maroon")
# print(colors)

# 8.extend():
# This method adds an entire list or any other collection datatype (set, tuple, dictionary)
# to the existing list.

# colors = ["voilet", "indigo", "blue"]
# rainbow = ["green", "yellow", "orange", "red"]

# colors.extend(rainbow)
# print(colors)

# Concatenating two lists:
colors = ["voilet", "indigo", "blue", "green"]
colors2 = ["yellow", "orange", "red"]

color = colors+colors2
print(color)