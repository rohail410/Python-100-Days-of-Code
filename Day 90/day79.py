class Animal:
    def __init__(self, group):
        self.group = group
    
    def showInfo(self):
        print(f"It belong to {self.group} group of Animal Kingdom.")
    
class Mammal:
    def __init__(self, category):
        self.category = category
        
    def showInfo(self):
        print(f"It belong to {self.category} category of Mammals.")
        

class Human(Mammal, Animal):
    def __init__(self, name, category="human", group="mammal"):
        self.name = name
        self.category = category
        self.group = group
        
    # def showInfo(self):
    #     print(f"The name of human is {self.name}.")

h1 = Human("Rohail")
h1.showInfo()
print(Human.mro())