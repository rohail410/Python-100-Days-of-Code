# listsingle= [1]
# print(type(listsingle))
# print(type(tupsingle))
# # print(tup1)
# # print(tup2)


# tup1 = (5, 2, 1, 5, 33, 12, 99, 43)
# tup2 = ("Red", "Yellow", "Green")
# tupsingle = (1,)

# if 33 in tup1:
#     print("Yes it is present")
# else: 
#     print("No it is not present")
    
# This script allows a user to input a list of integers. The user can add as many numbers as they want.
# Once the user finishes entering numbers, the script filters out all even numbers from the list,
# sorts the remaining odd numbers in descending order, and then prints the modified list.

# Taking a list as input

userList = []

userPermission = "y"

while(userPermission.lower() == "y"):
    # Taking the number from user 
    listItem = int(input("Give a number to be added to the list : "))
    # Add the number to the end of the list
    userList.append(listItem)
    
    # Ask for user permission to add more numbers
    userPermission = input("Do you want to add more numbers to the list (y/n) : ")
    
# printing the list taken from the user
print("Original List :", userList)

# using list comprehension to generate a new list of odd numbers only
oddList = [num for num in userList if num % 2 != 0]

# using sort function to sort the odd numbers in descending order

oddList.sort(reverse=True)

print("Sorted List of Odd Numbers :", oddList)
    
    