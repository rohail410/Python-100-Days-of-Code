"""
When a class is derived from another class, the child class will inherit all the public and protected properties and methods from the parent class. In addition, it can have its own properties and methods, this is called inheritance.
"""
class Employee:
    def __init__(self, name, id):
        self.name = name
        self.id = id
        
    def show(self):
        print(f"Information : {self.id} is {self.name}")
    
class Programmer(Employee):
    def showLanguage(self):
        print(f"{self.name} is Python Developer")

e1 = Employee("Haddiya Bibi", 100)

e2 = Employee("Rohail Boss", 200)

p1 = Programmer("Ayaan", 300)

e1.show()
e2.show()
p1.show()
print(p1.name)

p1.showLanguage()