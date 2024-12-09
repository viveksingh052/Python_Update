# if "__name__ == "__main__" in Python

# The if __name__ == "__main__" idiom is a common pattern used in Python scripts to determine whether the script
# is being run directly or being imported as a module into another script.

# 1.In Python, the __name__ variable is a built-in variable that is automatically
# set to the name of the current module..
# 2.In Python, the __name__ variable is a built-in variable that is automatically
# set to the name of the current module
# 3. When the script is imported as a module into another script, the __name__ variable is set to the name of the module.


import vivek
vivek.show()

# In summary, the if __name__ == "__main__" idiom is a common pattern used in Python scripts to determine whether the script is being run
# directly or being imported as a module into another script. It allows you to reuse
# code from a script by importing it as a module into another script, without
# running the code in the original script.