# Importing in Python is the process of loading code from a Python module
# into the current script.

# This allows you to use the functions and variables defined in the module
# in your current script, as well as any additional modules that the imported
# module may depend on.

# To import a module in Python, you use the import statement followed by the name
# of the module. 

# import math
# import numpy

# Once a module is imported, you can use any of the functions and
# variables defined in the module by using the dot notation

# import math

# result = math.sqrt(9)
# print(result)

# from keyword
# from math import sqrt , pi

# result = sqrt(9) *pi
# print(result)

# importing everything

# It's also possible to import all functions and variables from a module using the *
# wildcard. However, this is generally not recommended as it can lead to confusion
# and make it harder to understand where specific functions and variables are coming
# from.

# from math import *

# result = sqrt(9)
# print(result)  # Output: 3.0

# print(pi)  # Output: 3.141592653589793


# Python also allows you to rename imported modules using the as keyword.
# This can be useful if you want to use a shorter or more descriptive name 
# for a module, or if you want to avoid naming conflicts with other modules
#  or variables in your code.

# import math as m

# result = m.sqrt(9)*m.pi
# print(result)

# The dir function
# Finally, Python has a built-in function called dir that you can use to view the
# names of all the functions and variables defined in a module.
# This can be helpful for exploring and understanding the contents of a new module.

# import pandas as pd
# print(dir(pd))

# In summary, the import statement in Python allows you to access the functions
# and variables defined in a module from within your current script. You can
# import the entire module, specific functions or variables, or use the * wildcard
# to import everything. You can also use the as keyword to rename a module,
# and the dir function to view the contents of a module.

import vivek as v

v.show() #function
print(v.vivek) #variable
