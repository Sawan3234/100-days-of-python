#use of else in loops 

#for i in range(5):
    #print(i)
    #if i==4:
     #break
#else:
    #print("for loop has no access")
#Exception handling 
a=(input("Enter a number:"))
print("multiplication table of",a,"is:")
try:
  for i in range(1,11):
    print(int(a),"x",int(i),"=",int(a)*i)
except:
    print("inavalid input")
print("table  of",a)

try:
    number=int(input("enter your number:"))
    length=len(str(number))
    if(length==10):
      print(number)
    else:
        print("Invalid! enter a ten digit number:")
except ValueError:
    print("invalid number")
    print("enter the correct integer number")
    