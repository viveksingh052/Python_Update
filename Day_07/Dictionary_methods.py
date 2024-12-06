# 1.update()
aman = {"name":"vivek","section":"K20GR"}
aman.update({"age":23})
print(aman)

print("-"*80)

# Removing items from dictionary:
# 2.clear():

vivek ={1:"vivek",2:"shobhit",3:"pikki"}
# vivek.clear()
# print(vivek)

print("-"*80)

# 3.pop()
# The pop() method removes the key-value pair whose key is passed as a parameter.
vivek.pop(2)
print(vivek)

# 4.popitem():
# The popitem() method removes the last key-value pair from the dictionary.

aman.popitem()
print(aman)

# 5.del:
info = {'name':'Karan', 'age':19, 'eligible':True, 'DOB':2003}
del info['age']
print(info)

# student = {"name":"vivek","section":"B"}
# del  student
# print(student)

# If key is not provided, then the del keyword will delete the dictionary entirely.