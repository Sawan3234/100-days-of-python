#typecasting
a="1"
b="2"
#a=1
#b=2
print(a+b)
print(int(a)+int(b))
#explict(done via user) and implict typecasting(done by python)
string="16"
number=6
string_num=int(string)
sum=number+string_num
print("the sum of both numbers is:",sum)

#implicit (one data type is converted to another by python,converts lower data type to higher data type)
a=9
print(type(a))

b=60.6
print(type(b))

c=a+b
print(c)
print(type(c))
