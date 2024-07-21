#sets in python


#union in set
s1={1,2,3,4,5}
s2={6,2,8,3,10}
print(s1.union(s2))
print(s1.intersection(s2))
#symmetric difference
s1.symmetric_difference_update(s2)
print(s1)
item=s1.pop()
print(item)