for i in range(1,6):
    print(i)
    if i == 3:
        print("Breaking the loop")
        break
else:
    print("This is the else block in for loop")
    
    
i = 6
while i <= 10:
    print(i)
    i += 1
    if i == 8:
        print("Breaking the loop while")
        break
else:
    print("This is else block in while loop")