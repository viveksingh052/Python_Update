# x = 5

# def ms():
#     print(x)
#     y = 10
#     print(y)


# ms()
# print(y)

# we can access the global variable inside the function but we can't access the local variable globally


x = 10

def vivek():
    y = 5
    print(f"the value of the y is {y}")

    global x  #we can change the global variable inside the function using the global variable
    x = 11
    

print(f"the value of the x before running the function {x}")
vivek()
print(f"the value of the x after running the function {x}")

