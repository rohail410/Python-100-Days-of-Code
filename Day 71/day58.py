class Person:
    def __init__(self, n, o):
        print("I am a Person")
        self.name = n
        self.occ = o
        
    # name = "Harry"
    # occ = "Developer"
    
    def info(self):
        print(f"{self.name} is a {self.occ}")


a = Person("Rohail", "Gamer")
b = Person("Mehwish", "Cricketer")
c = Person(1, 2, 3)

a.info()
b.info()

# print(a.name)
# a.name = "Kanao"
# a.occ = "Hunter"
