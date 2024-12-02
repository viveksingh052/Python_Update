# do..while is a loop in which a set of instructions will execute at least once
# (irrespective of the condition) and then the repetition of loop's body will depend 
# on the condition passed at the end of the while loop. It is also known as an exit-controlled loop.

while True:
  number = int(input("Enter a positive number: "))
  print(number)
  if not number > 0:
    break