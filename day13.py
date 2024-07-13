#program to calculate the sum of first n natural numbers 
sum=0

a=int(input('enter positive numbers:'))
for i in range(1,a+1):
    sum +=i
print('sum of numbers :',sum)

#PRINT various pattern using nested loop
row=5
for i in range(1,row+1):
    for j in range(1,i+1):
        print('*',end="")
    print()

#sum of sqaures
sum=0
s=int(input('enter a number:'))
for i in range(1,s+1):
    sum+= i **2
print('the sum of square is:',sum)

        
