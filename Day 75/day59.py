"""
Python Decorators are powerful and versitile tool that allow you to modify the behavior of functions and methods. They are a way to extend the functionality of a function or method without modifying its source code.

A decorator is a function that takes another function as an argument and returns a new function that modifies the behavior of the orginal function. The new function is referred to as a "decorated" function. 
"""


# Decorator Defination 1
def greet(fx):
    def mfx(*args, **kwargs):
        print("Aoa, How are you, guys")
        fx(*args, **kwargs)
        print("Goodbye. Thank you for using this function")
    return mfx


# @greet
def hello():
    print("Hello World")

def sum(a, b):
    print(a + b)
    
greet(hello)()


greet(sum)(1, 10)

