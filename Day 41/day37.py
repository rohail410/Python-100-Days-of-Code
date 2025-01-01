def sum():
    try:
        num1 = int(input("Give first number: "))
        num2 = int(input("Give second number: "))
    except Exception as e:
        print(f"Error has occured : {e}")
        return 0
    else:
        print(num1 + num2)
        return 1
    finally:
        print("The execution is ended")

    print("THE EXECUTION IS ENDED")

result = sum()
print(result)