import time
t = time.strftime('%H:%M:%S')
# hour = int(time.strftime('%H'))
hour = int(input("Enter the hour: "))
if(hour>=0 and hour<12):
    print("Good Morning Bhai")
elif(hour>=12 and hour<17):
    print("Good AfterNoon Bro")
elif(hour>=17 and hour<0):
    print("Good Night")
print("Your time is",hour)

