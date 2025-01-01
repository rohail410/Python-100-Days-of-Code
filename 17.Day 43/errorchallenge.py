def division(num1, num2):
    """
    Perform division of two numbers with error handling
    
    Parameters:
    num1 (float, int or complex) The numerator
    num2 (float, int or complex) The denominator
    
    Returns:
    None
    """
    try:
        result = num1 / num2
    except ZeroDivisionError:
        print("Cannot Divide by Zero")
    except TypeError:
        print("Please Enter Valid Numbers")
    except Exception as e:
        print(f"Something went wrong: {e}")
    else:
        print(f"Your result is : {result}")
    finally:
        print("Execution has ended")
        
print(division.__doc__)

division(100, 10)  # Output => 10.0
division(40, 8.5)  # Output => 4.705882352941177
division(42, complex(10,2)) # Output => (4.038461538461538-0.8076923076923077j)

division(10, "a")  # Output => Please Enter Valid Numbers
division(10, 0) # Output => Cannot Divide by Zero