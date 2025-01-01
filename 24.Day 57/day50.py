f = open("file.txt2", "w")

lines = ["line 1", "line 2", "line 3", "line 4", "line 5"]

for line in lines:
    f.write(f"{line}\n")

f.close()




# lines = ["Hello Man\n", "How are you\n", "I am good"]

# f.writelines(lines)

# f.close()

# line1 = f.readline() 
# print(line1)
# line2 = f.readline() 
# print(line2)
# line3 = f.readline() 
# print(line3)
# line4 = f.readline() 
# print(line4)
# line5 = f.readline() 
# print(line5)
# line6 = f.readline() 
# print(line6)

# while True:
#     line = f.readline()
#     if not line:
#         break
#     print(line)