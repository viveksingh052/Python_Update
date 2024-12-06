# 1.isdisjoint():
# The isdisjoint() method checks if items of given set are present in another set.
# This method returns False if items are present, else it returns True.

set1 = {1,2,3,4,5}
set2 = {1,2,11,12,13}
set3 = {6,7,8,9,10}

print(set1.isdisjoint(set2))
print(set1.isdisjoint(set3))

print("-"*80)

# 2.issuperset():
# The issuperset() method checks if all the items of a particular set are present in the original set.
# It returns True if all the items are present, else it returns False.

city1 = {"kanpur","lucknow","aligarh"}
city2 = {"delhi","new delhi"}
city3 = {"lucknow","aligarh"}

print(city1.issuperset(city2))
print(city1.issuperset(city3))
print(city3.issuperset(city1))  #check if all the items of the calling set are present in the original set. here the calling set ie city3.

print("-"*80)

# 3.issubset()

num1 = {1,2,3,4}
num2 = {4,3,2,0}
num3 = {4,3,2,1}

print(num1.issubset(num2))
print(num1.issubset(num3))

print("-"*80)

# 4.add()

set10 = {1,2,3,4}
set10.add(9)
print(set10)

print("-"*80)

# 5.update()

set11 = {1,2,3,4,5,6}
set12 = {7,8,9,10}

set11.update(set12)
print(set11)

print("-"*80)

# 6.remove()/discard()
# We can use remove() and discard() methods to remove items form list.

set13 = {1,2,3,4}
set13.remove(4)
print(set13)
# set13.remove(5)
# print(set13)   #this gives an eroor 


set14 = {1,2,3,4}
set14.discard(4)
print(set14)

set14.discard(8)
print(set14)

print("-"*80)

# 7.pop()

# This method removes the last item of the set but the catch is that we don’t
# know which item gets popped as sets are unordered. However, you can access the 
# popped item if you assign the pop() method to a variable.


city = {"Tokyo", "Madrid", "Berlin", "Delhi"}
item = city.pop()
print(city)
print(item)

print("-"*80)

# 8.del()
# del is not a method, rather it is a keyword which deletes the set entirely.

# vivek = {"name","class"}
# del vivek
# print(vivek)

print("-"*80)

# 9.clear()
# This method clears all items in the set and prints an empty set.

aman = {1,2,3,4}
aman.clear()
print(aman)

print("-"*80)


# Check if item exists
# You can also check if an item exists in the set or not.

vivek = {"class","section","name"}

if "class" in vivek:
    print("Class is present in set vivek")
else:
    print("Sorry class is not present in set vivek")
