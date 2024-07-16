def fib(n):
    if(n<=1):
        return n
    else:
       return fib(n-1)+fib(n-2)
n=int(input("enter a number of terms ="))
print('fibannoic series of',n,'terms =')
for i in range(n):
    print(fib(i))
