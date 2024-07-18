#append add element in list
l=[16,55,44,4,16,1]
print(l)
l.append(10)
print(l)
#sort
l.sort()
print(l)
l.sort(reverse=True) #print in desending order
print(l)
#reverse() chage the original list
#l.reverse()
print(l)
print(l.index(44))
print(l.count(16))
#copy()
m=l.copy()
m[1]=16
print(m)
#inser()
m.insert(1,12)
print(m)
#extend()
m=['charles','lweis','max',]
l.extend(m)
p=l+m
print(p)
print(l)
