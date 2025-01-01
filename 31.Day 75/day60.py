""" 
Getters in Python are Methods that are used to access the values of an object's properties. They are used to return the value of a specific property and are typically defined using the @property decorator.
"""

""" 
It is important to note that getters do not take any parameters and we cannot set a value through getter method. For that we need a setter method which can be added by decorating method with @property_name.setter.

In conclusion, getters are a convenient way to access the values of an object's properties, while keeping the internal representation of the property hidden. This can be useful for encapsulation and data validation.
"""

class MyClass:
    def __init__(self, value):
        self._value = value
    
    def show(self):
        print(f"The value is {self._value}")
        
    @property
    def value(self):
        return self._value

    @value.setter
    def value(self, new_value):
        self._value = new_value
    
    
obj1 = MyClass(10)

obj1.show()
# obj1._value = 30
# print(obj1._value)

obj1.value = 23
print(obj1.value)

obj1.show()