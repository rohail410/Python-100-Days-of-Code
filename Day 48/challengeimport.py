# Importing datetime module in the current script
import datetime

# Using the now() function in the datetime module in the datetime class to print the current time
print(datetime.datetime.now()) # 2024-06-29 13:21:57.308394

# importing specific function from the math module and using as keyword for more detailed name for the sqrt function

from math import sqrt as square_root

print(square_root(9)) # Output => 3.0

# Using dir function to view all the function and variables defined in the math class

print(dir(datetime)) 

# Output => ['MAXYEAR', 'MINYEAR', 'UTC', '__all__', '__builtins__', '__cached__', '__doc__', '__file__', '__loader__', '__name__', '__package__', '__spec__', 'date', 'datetime', 'datetime_CAPI', 'time', 'timedelta', 'timezone', 'tzinfo']


# Importing the datetime module
import datetime

# Using the now() function from the datetime class to print the current date and time
print(datetime.datetime.now())  # Example Output: 2024-06-29 13:21:57.308394

# Importing the sqrt function from the math module and renaming it to square_root
from math import sqrt as square_root

# Using the renamed square_root function to calculate the square root of 9
print(square_root(9))  # Output: 3.0

# Using the dir() function to view all functions and variables defined in the datetime module
print(dir(datetime))  
# Output: ['MAXYEAR', 'MINYEAR', 'UTC', '__all__', '__builtins__', '__cached__', '__doc__', '__file__', '__loader__', '__name__', '__package__', '__spec__', 'date', 'datetime', 'datetime_CAPI', 'time', 'timedelta', 'timezone', 'tzinfo']
