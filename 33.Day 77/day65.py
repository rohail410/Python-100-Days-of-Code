""" 
Static methods in Python are methods that belong to a class rather than an instance of the class. They are defined using the @staticmethod decorator and do not have access to the instance of the class(i.e. self). They are called on the class itself, not on an instance of the class. Static methods are often used to create utility functions that don't need access to instance data.
"""


class Math:
    def __init__(self, num):
        self.num = num
    
    def addtoNum(self, n):
        self.num = self.num + n
    
    @staticmethod
    def add(a, b):
        return a + b
    
    
n1 = Math(5)
print(n1.num)

n1.addtoNum(6)
print(n1.num)

print(n1.add(1, 2))


