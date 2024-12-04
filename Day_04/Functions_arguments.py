#Functions arguments

# 1. DEFAULT Arguments

# def average(a,b):
#     print("The average is ",(a+b)/2)

# average(3,4)

# def average(a=6,b=6):
#     print("The average is ",(a+b)/2)

# average()

# def average(a=5,b=5):
#     print("The average is ",(a+b)/2)

# average(b=20)


# 2.Keyword Argument

# def name(fname, mname, lname):
#     print("Hello,", fname, mname, lname)

# name(mname = "Peter", lname = "Wesker", fname = "Jade")

# Hello, Jade Peter Wesker


# 3.Required Arguments

# def name(fname, mname, lname):
#     print("Hello,", fname, mname, lname)

# name("Peter", "Quill")


# name("Peter", "Quill")\
# TypeError: name() missing 1 required positional argument: 'lname'

# 4.Variable Length Arguments

# a.Arbitrary Arguments:

# def name(*name):
#     print("Hello",name[0],name[1],name[2])

# name("Vivek","Aman","Shobhit")

# Keyword Arbitrar Arguments:
def name (**name):
    print("Hello",name["first_name"],name["second_name"],name["last_name"])


name (first_name = "vivek",second_name = "aman", last_name = "singh")
