#passing argument in function
def sum(a,b):
    print("sum=",a+b)
sum(4,5)

#variable length argument
#we can pass multiple value to the function 
def sum(*numbers):
    sum=0
    for i in numbers:
        sum=sum+i
    print("sum is :",sum)
sum(4,5,6,18,45)