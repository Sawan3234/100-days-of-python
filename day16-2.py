#list in python
drivers=['leclerc','sainz','verstapen','norris','hamilton']
team=['ferrari','Redbull','maclaren','mercedes']

print(drivers)
print(team)
print(team[0],'=',drivers[0])
print(team[0],'=',drivers[1])
print(team[1],'=',drivers[2])
print(team[3],'=',drivers[4])

print(team[-1],'=',drivers[-2])
print(team[len(team)-3])
if "leclerc"in drivers and 'ferrari'in team:
    print("it is present")
else:
    print("not present")
#jump index
print(team[0:4:2])
#list comprehension
track=['barahin','miami','lasvegas','australia','monaco','saudi','japan','buddhapest','hungurian','silverstone','abu dhabi']
grandprix=[item for item in track if(len(item)>8)]
print(grandprix)