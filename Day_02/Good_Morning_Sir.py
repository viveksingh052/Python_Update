import time   #creating a program with the function 
def greet_user():
    timestamp = int(time.strftime('%H'))
    # we are using time.strftime() to get the current time.

    if(timestamp<12):
        greeting= "Good Morning"
    elif(timestamp<=12 and timestamp<18):
        greeting ="Good Afternoon"
    elif(timestamp<=18 and timestamp<22):
        greeting="Good Evening"
    else:
        greeting ="Good Night"
    
    print(greeting)

greet_user()


import time      #creating the program without the functions using only conditional statements
name = input("Enter your name:")

current_time = time.strftime('%H:%M:%S')
Current = int(time.strftime('%H'))

if(Current<12):
    print(name,"Good Morning")
elif(Current<=12 and Current<18):
    print(name,"Good Afternoon")
elif(Current<=18 and Current<22):
    print(name,"Good Evening")
else:
    print(name,"Good Night")