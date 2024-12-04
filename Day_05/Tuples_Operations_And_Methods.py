# Manipulating Tuples:
# Tuples are immutable, hence if you want to add, remove or change tuple items, then first you must
# convert the tuple to a list. Then perform operation on that list and convert it back to tuple.

names = ("vivek","aman","pikki","shobhit")

m = list(names)
print(type(m))

m.append("Kd")
print(m)

m.pop(2)
print(m)

names = tuple(m)
print(names)

# Thus, we convert the tuple to a list, manipulate items of the list using list methods, then
# convert list back to a tuple.


# Tuple methods:
# count() Method
# The count() method of Tuple returns the number of times the given element appears in the tuple.

# index() method
# The Index() method returns the first occurrence of the given element from the tuple.
