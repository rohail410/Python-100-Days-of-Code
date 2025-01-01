class Employee:
    def __init__(self, name, id):
        self.name = name
        self.id = id

    def show(self):
        print(f"The employee is {self.name} with id {self.id}.")
        
class Programmer(Employee):
    def __init__(self, name, id, lang):
        super().__init__(name, id)
        self.lang = lang
    
    def show(self):
        print(f"The employee is {self.name} with id {self.id} and is programmer and language is {self.lang}.")
        super().show()
    


e1 = Employee("Rafay", 100)
e1.show()

p1 = Programmer("Rohail", 200, "Python")
p1.show()

