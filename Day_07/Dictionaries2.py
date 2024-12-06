student = {"name":"vivek","section":"K20GR"}

for key in student.keys():
    print(student[key])

print("-"*80)

for values in student.values():
    print(values)

print("-"*80)

for key,value in student.items():
    print(f"The value of key is {key} and value is {value}")

print("-"*80)