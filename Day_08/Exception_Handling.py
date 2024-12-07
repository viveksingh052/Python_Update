try:
    num = int(input("Enter an integer: "))
except ValueError:
    print("Number is not an integer")


# try….. except blocks are used in python to handle errors and exceptions.
# The code in try block runs when there is no error. If the try block catches
# the error, then the except block is executed.