# Making a list

num_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# Task 1 : Given a list of numbers, use map with a lambda function to create a new list with each number squared

square_list = map(lambda x : x * x, num_list)

print(list(square_list)) # Output => [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]

# Task 2 : Use filter to Find Even Numbers: Use filter with a lambda function to filter out all the odd numbers from a list, keeping only the even numbers.

even_list = filter(lambda x : x % 2 == 0, num_list)

print(list(even_list)) # Output => [2, 4, 6, 8, 10]

# Task 3 : Use reduce to Calculate the Product of Numbers: Use reduce with a lambda function to calculate the product of all numbers in a list

from functools import reduce

product = reduce(lambda x , y : x * y, num_list) 

print(product) # Output => 3628800





