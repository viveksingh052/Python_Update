# Recursion in python:
# Recursion is the process of defining something in terms of itself.
# When a function call itself it is called Recursion 


def factorial(num):
    if(num==1 or num==0):
        return 1
    else:
        return(num* factorial(num-1))

num = 3
print("Number: ",num)
print("Factorial: ",factorial(num))

