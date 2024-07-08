#string operations
a='houseOFthedragon???? ice n fire'
print(len(a))
#uppercase (upper())
print(a.upper())
#lowecase (lower()) convert the string to lower case
print(a.lower())
#rstrip() remove trailing characters
print(a.rstrip("?"))
#replace()replace all occurance of a string with another string
print(a.replace('houseOFthedragon','danceofdragon'))
#split() splits the given string and returns the seperated string as list items
print(a.split(" "))
#capitalize() turns only the first character of the string to uppercase and the rest other characters of the string are turned to lowercase.
blog="introduction tO the python"
print(blog.capitalize())
#center() aligns the string to the center as per the parameters given by the user
print(len(blog.center(50)))
print(len(blog))
#endswith() checks if the string ends with given value
#returns boolean values
print(a.endswith("????",16,22))
#find()searches for the first occurrence of the givrn value and returns the index where it is present.
str1='she is the mother of dragons.She is beautiful women'
print(str1.find('is'))
#index() raises an exception if the given value id absent from the string
#print(str1.index('ishh'))
#isalnum() returns true only if the entire string only consists of A-Z,a-z,0-9.return false if any other characters.
b='mynameissawan'
c='my ID is sawan@3234'
print(b.isalnum())
print(c.isalnum())
#isalpha() only alphabets not numbers
print(b.isalpha())
#islower()checks if the strings are in lower case or not.
print(c.islower())
#isprintable()returns true if all the value within the given string are printable.
d="we wish you \n"
print(d.isprintable())
#istitle() returns true if the first letter of each word of the string is capitalized
t="house Of the Dragon"
print(t.istitle())
#startswith()similar to ends with
print(t.startswith('House'))
#swapcase()changes upper to lower and vice versa
print(t.swapcase())
#title() capitalizes each letter of the word 
print(t.title())