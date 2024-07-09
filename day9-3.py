#Nested if statement
#check whether the given number is positive or negative and find the range of numer like 1-10 10-20
num=int(input('enter a number:'))

if(num<0):
    print('number is negative')
elif(num>0):
    if(num<=10):
        print("numberis positive & lies between 1-10")
    elif(num>=20):
        print('number is positive & lies bewteen 10-20')
    else:
        print('number is  positive but grater than 20')
else:
    print('number is zero')