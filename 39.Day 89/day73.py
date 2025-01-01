class Employee:
    def __init__(self, name, id):
        self.name = name
        self.id = id
    
    def __str__(self):
        return f"The employee name is {self.name} with id {self.id}."
    
    def __repr__(self):
        return f"Employee('{self.name}',{self.id})"
    
    def __call__(self):
        print("This is an executable object.")

e1 = Employee("Rohail", 100)

print(str(e1))
print(e1)

print(repr(e1))

e1()
