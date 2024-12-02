# Break Statement
# The break statement enables a program to skip over a part of the code.
# A break statement terminates the very loop it lies within.

for i in range(1,20):
    if(i==11):
        break
    print(i,"vivek")

#Continue Statement
# The continue statement skips the rest of the loop statements and causes the next iteration to occur.

for i in [2,4,5,6,7,8,10,0]:
    if(i%2 !=0):
        continue
    print(i)

