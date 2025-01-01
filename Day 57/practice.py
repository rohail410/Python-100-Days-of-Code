f = open("file.txt", "r")

# f.write("\nHello Boy")

content = f.read()
print(content)

f.close()

# with open("file.txt", "r+") as f:
#     f.write("Hello Rohail")
#     content = f.read()
#     print(content)