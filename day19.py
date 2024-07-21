#fstring solved the problem of string formating
letter="hey driver{1} is currentyly in position{0}"
position="first"
name="max verstapen"
#print(letter.format(name,position))
print(f"hey driver{name} is currentyly in position{position}")

#doc string
def str(n):
     '''Takes input n and multiply it with n to find the square'''
     print(n*n)
str(5)
print(str.__doc__) 