# def sum(a, b, c):
#     return a + b + c

# def sum(a, b):
#     if (a == 1):
#         return b
#     elif (b == 1):
#         return a
#     return a + b

# ans = sum(10, 1)
# print(ans)

# ans = sum(1 , 2, 3)
# print(ans)

# Creating a function for  calculating a factorial
def Findfactorial(num):
    
    # Handling exceptional cases
    if (num == 0):
        return 1
    elif (num < 0):
        return "Negative numbers do not have a factorial"
    
    # Running a loop to calculate the factorial of number by multiply numbers for 1 to num and storing the product in factorial variable
    factorial = 1
    for i in range(1, num+1):
        factorial = factorial * i
    
    return factorial

ans = Findfactorial(5)
# Printing the factorial of num
print(ans)

# Creating a function for calculating a factorial
def find_factorial(num):
    
    # Handling exceptional cases
    if num == 0:
        return 1
    elif num < 0:
        return "Negative numbers do not have a factorial"
    
    # Running a loop to calculate the factorial of number by multiplying numbers from 1 to num and storing the product in factorial variable
    factorial = 1
    for i in range(1, num + 1):
        factorial *= i
    
    return factorial

# Calculating and printing the factorial of 5
ans = find_factorial(5)
print(ans)  # Output: 120
