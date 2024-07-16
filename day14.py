#break statement
for i in range (15):
  
  if(i==6):
      print("skip the iteration")
      continue
  print("9 x",i+1,"=",9*(i+1))
  if(i==9):
      break
    
    
#do while loop emulation


while True:
    a=int(input("enter numbers:"))
    print (a)
    if(a<0):
        break