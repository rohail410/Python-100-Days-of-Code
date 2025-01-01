# # Creating a function for Fibonnaci sequence

# def fibo_seq (position):
#     if position == 0:
#         return 0
#     elif position == 1:
#         return 1
#     else:
#         return fibo_seq(position - 1) + fibo_seq(position - 2)
    

# print(fibo_seq(6))


# Creating a function for Fibonacci sequence

def fibo_seq(position):
    # Base case: position 0 returns 0
    if position == 0:
        return 0
    # Base case: position 1 returns 1
    elif position == 1:
        return 1
    # Recursive case: sum of the two preceding numbers
    else:
        return fibo_seq(position - 1) + fibo_seq(position - 2)

# Test the function with position 6
print(fibo_seq(6)) # Output => 8
