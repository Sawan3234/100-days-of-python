#n=input("enter ypur phone number:")
#if(len(n)<=10):
   # raise ValueError("invalid number")
a=input("enter any value between 5 and 9:")
if(a<"5" or a>"9" and a.strip().lower()!="quit"):
   raise ValueError("value should be between 5 and 9")
print("worked")