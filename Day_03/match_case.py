x = int(input("Enter the number:"))

match x:
    case 0:
        print("x i zero")
    
    case 4 if(x%2==0):
        print("x%2==0 and case is 4")
    
    case _ :
        print(x ,"pattern not matches")
    

