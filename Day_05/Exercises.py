# Create a program capable of displaying questions to the user like KBC.
# Use List data type to store the questions and their correct answers.
# Display the final amount the person is taking home after playing the game.

# print("Welcome to KBC")
# print("Which Langauge has indentation as well as dynamically typed langauge?")
# "\n"
# print("Here are your options:")
# lang_names = ["1. java","2. python","3. c","4. cpp"]

# print(lang_names , sep='   ,     ')
# var1 = input("Enter your answer: ")

# if var1 == "python":
#     print("Correct Answer,You won 1 crore")
# else:
#     print("Wrong Answer, You are eliminated")



print("Welcome to the KBC, Kaun Banega Crorepati")
Question = ["Who is the national bird of India?","Which is the national sport of India?","Which is the Capital of India?"]

while(True):
    
    print("Apka Phela Sawal Screen Par or Yeh rhe options")
    print(Question[0])

    Options = ["A.Parrot","B.Duck","C.Pigeon","D.Peacock"]
    print(Options[0])
    print(Options[1])
    print(Options[2])
    print(Options[3])

    user = input("Enter your ans:")

    if user == "D":
        print("Aap Jeet gye hai 5000")
    
    else:
        print("Apne diya hai galat jawab")
        break

    "\n"
    "\n"
    print("Apka agla sawal screen par!")



    print("-"*50)

    "\n"
    "\n"

    print(Question[1])

    Options = ["A.Cricket","B.BasketBall","C.Hockey","D.Tennis"]
    print(Options[0])
    print(Options[1])
    print(Options[2])
    print(Options[3])

    user = input("Enter your ans:")

    if user == "C":
        print("Aap Jeet gye hai 10000")
    
    else:
        print("Apne diya hai galat jawab")
        print("Aap Jeete hai 5000 Ruppee ")
        break

    "\n"
    "\n"
    print("Apka agla sawal screen par!")
     
    
    "\n"
    "\n"

    print(Question[2])

    Options = ["A.Delhi","B.Kerala","C.Orissa","D.Assam"]
    print(Options[0])
    print(Options[1])
    print(Options[2])
    print(Options[3])

    user = input("Enter your ans:")

    if user == "A":
        print("Aap Jeet gye hai 20000")
        print("Game Yhi Samapt Hota hai aap jeet gye hai dhanrashi 20000 Ki. Congratulations!!")
        break
    
    else:
        print("Apne diya hai galat jawab")
        print("Aap jeete hai 1000 Ruppee")
        break

    "\n"
    "\n"
    print("Apka agla sawal screen par!")



    print("-"*50)



