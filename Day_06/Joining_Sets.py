#Union and Update()
# set1 = {"aman","vivek",1,2}
# set2 = {"singh","kumar",3,4}

# set3 =print(set1.union(set2))

# set1.update(set2)
# print(set1)

# The union() and update() methods prints all items that are present in the two sets.
# The union() method returns a new set whereas update() method adds item into the existing set from
# another set.

#Intersection and Intersection_update():
# The intersection() and intersection_update() methods prints only items that are similar to both the sets.
# The intersection() method returns a new set whereas intersection_update() method updates into the 
# existing set from another set.


# cities = {"Tokyo", "Madrid", "Berlin", "Delhi"}
# cities2 = {"Tokyo", "Seoul", "Kabul", "Madrid"}
# cities3 = cities.intersection(cities2)
# print(cities3)

# cities = {"Tokyo", "Madrid", "Berlin", "Delhi"}
# cities2 = {"Tokyo", "Seoul", "Kabul", "Madrid"}
# cities.intersection_update(cities2)
# print(cities)

# III. symmetric_difference and symmetric_difference_update():
# The symmetric_difference() and symmetric_difference_update() methods prints only items that are 
# not similar to both the sets. The symmetric_difference() method returns a new set whereas
# symmetric_difference_update() method updates into the existing set from another set.

# cities = {"Tokyo", "Madrid", "Berlin", "Delhi"}
# cities2 = {"Tokyo", "Seoul", "Kabul", "Madrid"}
# cities3 = cities.symmetric_difference(cities2)
# print(cities3)

# cities = {"Tokyo", "Madrid", "Berlin", "Delhi"}
# cities2 = {"Tokyo", "Seoul", "Kabul", "Madrid"}
# cities.symmetric_difference_update(cities2)
# print(cities)

# difference() and difference_update():
# The difference() and difference_update() methods prints only items that are only present
# in the original set and not in both the sets. The difference() method returns a new set
# whereas difference_update() method updates into the existing set from another set.

# cities = {"Tokyo", "Madrid", "Berlin", "Delhi"}
# cities2 = {"Seoul", "Kabul", "Delhi"}
# cities3 = cities.difference(cities2)
# print(cities3)

# cities = {"Tokyo", "Madrid", "Berlin", "Delhi"}
# cities2 = {"Seoul", "Kabul", "Delhi"}
# print(cities.difference(cities2))