#functions
def factorial(n):
    if(n==1):
       return n
    else:
       return n*factorial(n-1)

n=int(input("enter a positive number:"))
fact=factorial(n)
print("factorial of ",n,'=',fact)

