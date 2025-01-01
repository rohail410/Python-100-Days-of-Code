# # Create two list of random email

# list1 = ["alice@example.com", "bob@example.com", "carol@example.com", "alice@example.com"]
# list2 = ["dave@example.com", "carol@example.com", "eve@example.com", "bob@example.com"]

# # Task 1: Given two lists of email addresses, list1 and list2, convert them to sets to remove any duplicate email addresses within each list.

# set1 = set(list1)
# set2 = set(list2)

# print(set1) # {'carol@example.com', 'bob@example.com', 'alice@example.com'}
# print(set2) # {'carol@example.com', 'eve@example.com', 'bob@example.com', 'dave@example.com'}

# # Task 2: Find the common email addresses (i.e., email addresses that appear in both sets).

# commonEmails = set1.intersection(set2)
# print(commonEmails) # {'carol@example.com', 'bob@example.com'}

# # Task 3: Find the unique email addresses in list1 that do not appear in list2.

# uniqueEmailsList1 = set1.difference(set2)
# print(uniqueEmailsList1) # {'alice@example.com'}

# # Task 4: Combine all unique email addresses from both lists into a single set.

# uniqueEmailbothList = set1.symmetric_difference(set2)
# print(uniqueEmailbothList) # {'dave@example.com', 'eve@example.com', 'alice@example.com'}



# Create two lists of random email addresses
list1 = ["alice@example.com", "bob@example.com", "carol@example.com", "alice@example.com"]
list2 = ["dave@example.com", "carol@example.com", "eve@example.com", "bob@example.com"]

# Task 1: Convert lists to sets to remove duplicate email addresses within each list
set1 = set(list1)
set2 = set(list2)

print("Set 1:", set1)  # Output: {'carol@example.com', 'bob@example.com', 'alice@example.com'}
print("Set 2:", set2)  # Output: {'carol@example.com', 'eve@example.com', 'bob@example.com', 'dave@example.com'}

# Task 2: Find the common email addresses (i.e., email addresses that appear in both sets)
common_emails = set1.intersection(set2)
print("Common Emails:", common_emails)  # Output: {'carol@example.com', 'bob@example.com'}

# Task 3: Find the unique email addresses in list1 that do not appear in list2
unique_emails_list1 = set1.difference(set2)
print("Unique Emails in List 1:", unique_emails_list1)  # Output: {'alice@example.com'}

# Task 4: Combine all unique email addresses from both lists into a single set
all_unique_emails = set1.union(set2)
print("All Unique Emails:", all_unique_emails)  # Output: {'carol@example.com', 'bob@example.com', 'alice@example.com', 'eve@example.com', 'dave@example.com'}
