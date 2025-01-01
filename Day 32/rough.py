# # Task 1 : Creating a tuple
# tup1 = (23, 5, 10, 15, 25, 30, 35, 40, 45, 50)

# # Task 2 : Finding the index of element 30 in tuple
# print(tup1.index(30)) # Output = 5

# # Task 3 : Creating a new tuple by merging orginal with another one: (60, 70, 80)

# # Creating new tuple
# tup2 = (60, 70, 80)

# mergedtuple = tup1 + tup2

# print(mergedtuple)

# # Printing the length of merged of merged tuple
# print(len(mergedtuple)) # Output = 13



# Task 1: Creating a tuple
tup1 = (23, 5, 10, 15, 25, 30, 35, 40, 45, 50)

# Task 2: Finding the index of element 30 in the tuple
print(tup1.index(30))  # Output: 5

# Task 3: Creating a new tuple by merging the original with another one: (60, 70, 80)

# Creating the new tuple
tup2 = (60, 70, 80)

# Merging the tuples directly
merged_tuple = tup1 + tup2

# Printing the merged tuple
print(merged_tuple)  # Output: (23, 5, 10, 15, 25, 30, 35, 40, 45, 50, 60, 70, 80)

# Printing the length of the merged tuple
print(len(merged_tuple))  # Output: 13


print("Values")
print(tup1[0])
print(tup1[1])
print(tup1[2])
print(tup1[3])