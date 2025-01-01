def sum(a, b):
    print(a + b)
    
def subtract(a, b):
    print(a - b)
    
def welcome():
    print("Welcome")
    


welcome()

a = int(input("Give the first number : "))
b = int(input("Give the second number : "))

opt = input("Which operation you want to perform: + or - : ")

if (opt == "+"):
    sum(a, b)
elif(opt == "-"):
    subtract(a,b)
else:
    print("invalid operator")

welcome()
