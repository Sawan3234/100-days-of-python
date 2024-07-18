#tupple
tup=(1,5,"string")
print(type(tup),tup)
print(tup[0])
if "strings" in tup:
    print("it is prsesnt")
else:
    print("not present")
tup2=tup[:] #tuple slicing
print(tup2)