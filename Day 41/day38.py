def seq():
    num = int(input("Give a num : "))
    if num < 5 or num > 9:
        raise ValueError("Value not in range")
    return num

try:
    result = seq()
    print(result)
except ValueError as e:
    print(e)

num = int(input("Give a number between 5 and 9 : "))

if num < 5 or num > 9:
    raise ValueError("Number is not between 5 and 9")
