#elif statements
a=int(input('enter your budget:'))
p=int(input('enter product price:'))

if(p==a):
    print("product is in budget:")
elif(p-a<=10):
    print("little over budget but affordable")
elif(p-a<=50):
    print("over budget have to think twice")
else:
    print("aaukat se bahar hai nikal jao :)")

