def gmean(a,b):
    mean = a*b/(a+b)
    print(mean)

def isgreat(a,b):
    if(a>b):
        print("First number is  Greater than Second Number")
    elif(b>a):
        print("Second number is Greater than First Number")
    else:
        print("Both are equal")




a = 5
b = 4

gmean(a,b)

c= 7
d = 8
gmean(c,d)


e = 8
f = 9

isgreat(e,f)

g = 10
h = 10

isgreat(g,h)
