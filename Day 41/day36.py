try:
    num1 = int(input("Give first number: "))
    num2 = int(input("Give second number: "))
except Exception as e:
    print(f"Error has occured : {e}")
else:
    print(num1 + num2)

num0 = int(input("GIVE WRONG NUMBER !!!!!!!!!: "))

try:
    num1 = int(input("Give first number: "))
    num2 = int(input("Give second number: "))
except Exception as e:
    print(f"Error has occured : {e}")
else:
    print(num1 * num2)

try:
    num1 = int(input("Give first number: "))
    num2 = int(input("Give second number: "))
except Exception as e:
    print(f"Error has occured : {e}")
else:
    print(num1 - num2)
