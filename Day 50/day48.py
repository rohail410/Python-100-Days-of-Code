x = 10 # global variable

def my_function():
    global x
    x = 5 # this will change the value of the global variable x
    

my_function()
print(f"X = {x}") # prints 5

