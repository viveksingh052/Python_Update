# set_methods

# 1.union() and update()

set1 = {1,2,3,4,5}
set2 = {6,7,8,9,10}

print(set1.union(set2))
set1.update(set2)
print(set1) 

print("-"*80)

# 2.intersection() and intersection_update()

set3 = {1,2,3,4,5}
set4 = {5,4,3,6,7}

print(set3.intersection(set4))
set3.intersection_update(set4)
print(set3)

print("-"*80)

# 3.symmetric_difference() and symmetric_difference_update():

set5 = {1,2,3,4,5}
set6 = {1,2,3,7,8}

print(set5.symmetric_difference(set6))

set5.symmetric_difference_update(set6)
print(set5)

print("-"*80)

# 4.difference() and difference_update()
set7 = {1,2,3,4,5}
set8 = {6,7,8,1,2,3}

print(set7.difference(set8))
set7.difference_update(set8)
print(set7)


