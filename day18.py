#tupple operations
#tuple concatination
tuple1=('charles','carlos','lando','piastri','verstapen','perez','hamilton','russel','alonso','stroll')
tuple2=('riccardo','tsunoda','alobon','sergent','hulkinberg','magnessun','zhyou','bottas','gasly','ocon')
tuple=tuple1+tuple2
print(tuple)

#tuple count
tuple=(16,55,1,4,10,16,44,11,16,16)
num=tuple.count(16)
print("count of ",16,"=",num)

#index() method
ind=tuple.index(16,1,7)
print("index:",ind)