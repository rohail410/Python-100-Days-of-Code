import time

# clocktime = int(input("Tell the hour on the clock : "))

clocktime = time.localtime().tm_hour
print(type(clocktime))

if (clocktime >= 5 and clocktime <= 11):
    print("Good Morning")
elif (clocktime > 11 and clocktime <= 17):
    print("Good Afternoon")
elif (clocktime > 17 and clocktime <= 21):
    print("Good Evening")
else:
    print("Good Night")
    