import time
t=time.strftime('%H:%M:%S')
hour=int(time.strftime('%H'))
hour=int(input('enter hour:'))
print ('hour:',hour)
min=int(time.strftime('%M'))
print('min:',min)
sec=int(time.strftime('%S'))
print('second:',sec)
if(hour>=0 and hour<12):
    print("good morning ")
elif(hour>=12 and hour<17):
    print("good afternoon")
else:
    print("good night")
print("time is =",hour,':',min,':',sec)