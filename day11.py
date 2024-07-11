#match case statements
#like switch case in c .
# A simple calculator
a=int(input("enter a number:"))
b=int(input("enter a number:"))
print("1.Add 2.Sub 3.multiply 4.Divide")
ch=int(input('enter your choice'))
match ch:
    case 1:
        add=a+b
        print("sum:",add)
    case 2:
        sub=a-b
        print("subtraction:",sub)  
    case 3:
        mul=a*b
        print("multiplication:",mul)
    case 4:
        div=a/b 
        print("Division:",div)
    case _:
        print("invalid choice") 