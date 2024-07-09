#if else statements
#conditional operators 
#>,<,>=,<=,==,!=
a=int(input("enter your age"))
print("your age is :",a)
if(a>18):
    print("you can drive")
else:
    print("you cannot drive")
    print('less')
    
    
print(a<18)
print(a>18)
print(a<=18)
print(a>=18)
print(a!=18)

product=1500.2018
budget=1500.10
if(product==budget):
    print("buy the product")
elif(product>=budget):
    print("increase your budget")
else:
    print("over the budget")