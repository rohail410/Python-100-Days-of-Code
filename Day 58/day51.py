with open("file1.txt", "w+") as f:
    f.write("12345678910")
    
    f.seek(5)
    
    print(f.tell())
    
    content = f.read()
    print(content)
    

with open("file2.txt", "w+") as f:
    f.write("Hello Darkness My Old Friend")
    
    content2 = f.readline()
    print(content2)
    
    # content = f.read()
    # print(content)
    
    # f.truncate(5)
    
    # content = f.read()
    # print(content)
        

with open("file2.txt", "r") as f:
    content = f.read()
    print(content)



