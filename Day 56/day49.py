f = open("myfile.txt", "r")
# print(f)

text= f.read()
print(text)
f.close()

f2 = open("myfile2.txt", "a")
f2.write("\nFile 2")
f2.close()

