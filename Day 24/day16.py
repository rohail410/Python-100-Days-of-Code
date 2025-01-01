# # Match Case Statement

# x = 4

# match x:
#     # if x is 0
#     case 0:
#         print("x is zero")
    
#     # case with if-condition
#     case 4 if x % 2 == 0:
#         print("x % 2 == 0 and case is 4")
    
#     # Empty case with if-condition
#     case _ if x < 10:
#         print("x is < 10")
        
#     # default case (will only be matched if the above cases were not a match)
#     # so it is basically an else
#     case _:
#         print(x)

# Match Case Statement

weekday_number = 3

match weekday_number:
    case 1:
        print("Monday")
    case 2:
        print("Tuesday")
    case 3:
        print("Wednesday")
    case 4:
        print("Thursday")
    case 5:
        print("Friday")
    case 6:
        print("Saturday")
    case 7:
        print("Sunday")


