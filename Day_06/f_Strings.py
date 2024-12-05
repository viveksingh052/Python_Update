# String formatting in python
# String formatting can be done in python using the format method.

letter = "Hey! My name is {} and I am from {}."
country = "India"
name = "Vivek"

print(letter.format(name,country))#format method
print(f"Hey! My name is {name} and I amd from {country}.") #FStrings
print(f"Hey! My name is {{name}} and I amd from {{country}}.") #To show FStrings looks like


price = 39.09999
print(f"The price should be {price:.2f}")
# It is a new string formatting mechanism introduced by the PEP 498. It is also known as Literal String Interpolation or more
# commonly as F-strings (f character preceding the string literal). The primary focus of this mechanism is to make the interpolation easier.

val = 'Geeks'  
print(f"{val}for{val} is a portal for {val}.") 

name = 'Tushar'  
age = 23  
print(f"Hello, My name is {name} and I'm {age} years old.")

print(f"{2 * 30}")


