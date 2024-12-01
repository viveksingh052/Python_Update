# upper  The upper() method converts a string to upper case.
# name = "vivek"
# print(name.upper())

# lower The lower() method converts a string to lower case.
# name = "VIVEK"
# print(name.lower())

# strip The strip() method removes any white spaces before and after the string.
# name = "    vivek    "
# print(name.strip())

# rstrip the rstrip() removes any trailing characters (it removes the trailing characters only from the end)
# name = "!!!!Vivek!!!!"
# fname = "Vivek!!!!"
# print(name.rstrip('!'))
# print(fname.rstrip('!'))

# replace The replace() method replaces all occurences of a string with another string
# name = "vivek Singh"
# print(name.replace("v","s"))

# split The split() method splits the given string at the specified instance and 
# the separated strings as list items.
# name = "Vivek Singh"
# print(name.split(" "))

# capitalize The capitalize() method turns only the first character of the string to uppercase and the
# rest other characters of the string are turned to lowercase. The string has no effect if the first 
# character is already uppercase.
# name = "vivek singh"
# print(name.capitalize())
# name = "vivek SinGH" ******************************************
# print(name.capitalize())***************************************

# center The center() method aligns the string to the center as per the parameters given by the user.
# name = "vivek singh"
# print(name.center(50))

# We can also provide padding character. It will fill the rest of the fill characters provided by the 
# user
# print(name.center(50,"."))

# count The count() method returns the number of times the given value has occurred within the given string.
# name = "vivek singh"
# print(name.count("v"))

# endswith  The endswith() method checks if the string ends with a given value. If yes then return True, else
# return False.
# name = "vivek singh !!!"
# print(name.endswith("!"))

# We can even also check for a value in-between the string by providing start and end index positions.
# sentence = "Vivek is a good boy!!!!"
# print(sentence.endswith("is",3,8))

# find The find() method searches for the first occurrence of the given value and returns the
# index where it is present. If given value is absent from the string then return -1
# sentence = "He playes very well !"
# print(sentence.find("es"))
# print(sentence.find("mu"))
# As we can see, this method is somewhat similar to the index() method. The major
# difference being that index() raises an exception if value is absent whereas find() does not.

# index The index() method searches for the first occurrence of the given value and returns
# the index where it is present. If given value is absent from the string then raise an exception.
# str = "vivek is a good boy!"
# print(str.index("is"))
# print(str.index("m"))

# isalnum The isalnum() method returns True only if the entire string only consists of
# A-Z, a-z, 0-9. If any other characters or punctuations are present, then it returns False.
# str = "viveksinghaman"
# str1 = "viveksinghaman "
# str2 = "vivek\"\"singhaman"
# print(str.isalnum())
# print(str1.isalnum())
# print(str2.isalnum())

#isalpha The isalnum() method returns True only if the entire string only consists of A-Z, a-z.
# If any other characters or punctuations or numbers(0-9) are present, then it returns False
# name = "viveksingh"
# name1 = "123vivek"
# name2 = "vivek singh"
# print(name.isalpha())
# print(name1.isalpha())
# print(name2.isalpha())

# islower The islower() method returns True if all the characters in the string are lower case,
#  else it returns False.
# name = "vivek singh"
# name1 = "VivekSingh"
# name2 = "VIVEKSINGH"
# print(name.islower())
# print(name1.islower())
# print(name2.islower())

#isprintable The isprintable() method returns True if all the values within the given string are
# printable, if not, then return False.
# name = "vivek singh is a good boy"
# print(name.isprintable())

# Non-printable characters:
# Control characters (e.g., \n, \t, \r, \x00 for null)
# Characters with ASCII values below 32, except for space..

# name = "vivek\nsingh"
# name1 = "vivek\tsingh"
# name2 = "vivek\x00singh"
# print(name.isprintable())
# print(name1.isprintable())
# print(name2.isprintable())

# isspace The isspace() method returns True only and only if the string contains white spaces,
# else returns False.
# space = "         " #using spacebar
# space1 = "          " #using tab
# space2 = "    vivek     "
# print(space.isspace())
# print(space1.isspace())
# print(space2.isspace())

# istitle The istitile() returns True only if the first letter of each word of the string
# is capitalized, else it returns False.
# name = "Vivek Singh"
# name1 = "vivek Singh"
# name2 = "Vivek singh"
# print(name.istitle())
# print(name1.istitle())
# print(name2.istitle())

# isuppercase The isupper() method returns True if all the characters in the string are 
# upper case, else it returns False.
# name = "Vivek Singh"
# name1 = "VIVEK SINGH"
# print(name.isupper())
# print(name1.isupper())

# startswith The endswith() method checks if the string starts with a given value. If yes
# then return True, else return False.
# name = "vivek singh"
# print(name.startswith("viv"))
# print(name.startswith("ses"))

# swapcase The swapcase() method changes the character casing of the string. Upper case are 
# converted to lower case and lower case to upper case.
# name = "vIVEK sINGH"
# print(name.swapcase())

# title() The title() method capitalizes each letter of the word within the string.
# name = "vivek singh is a very good boy"
# print(name.title())