import time

# number of seconds passed since epoch
print(time.time())

# takes second passed since epoch as an arguemnt and returns a string
print(time.ctime())


#suspends execution of the current thread for the given number of seconds
# print("Printed immediately.")
# time.sleep(2.4)
# print("Printed after 2.4 seconds.")

# takes the number of seconds passed since epoch as an argument and returns strut_time
print(time.localtime())

print(time.localtime().tm_year)
print(time.localtime().tm_year)