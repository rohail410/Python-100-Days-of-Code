# Open a file named "example.txt" in write mode
f = open("example.txt", "w")

# Write multiple lines to the file
f.write("Hello.\nThis is an example file\nWe are learning about File I/O\n")

# Close the file
f.close()

# Open the file in append mode using a context manager
with open("example.txt", "a") as f:
    # Write an additional line at the end of the file
    f.write("Adding another line in the end\n")

# Open the file in read mode using a context manager
with open("example.txt", "r") as f:
    # Read the entire content of the file
    content = f.read()
    # Print the content to the console
    print(content)

# Open a file named "example2.txt" in write mode
f2 = open("example2.txt", "w")

# List of lines to be written to the file
lines = ["line 1\n", "line 2\n", "line 3\n"]

# Write the list of lines to the file using a context manager
with open("example2.txt", "w") as f:
    f.writelines(lines)

# Open the file in read mode using a context manager
with open("example2.txt", "r") as f:
    # Loop through each line in the file
    while True:
        # Read a single line from the file
        line = f.readline()
        # If the line is empty, break the loop (end of file)
        if not line:
            break
        # Print the line to the console
        print(line)


























# f = open("example.txt", "w")

# f.write("Hello.\nThis is an example file\nWe are learning about File I/O\n")

# f.close()

# with open("example.txt", "a") as f:
#     f.write("Adding another line in the end\n")
    

# with open("example.txt", "r") as f:
#     content = f.read()
#     print(content)
    
    
# f2 = open("example2.txt", "w")

# lines = ["line 1\n", "line 2\n", "line 3\n"]

# with open("example2.txt", "w") as f:
#     f.writelines(lines)

# with open("example2.txt", "r") as f:
#     while True:
#         line = f.readline()
#         if not line:
#             break
#         print(line)
        































