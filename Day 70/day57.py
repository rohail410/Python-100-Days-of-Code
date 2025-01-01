class Person:
    name = "Harry"
    occupation = "Software Developer"
    networth = 10
    def info(self):
        print(f"{self.name} is a {self.occupation}")
        
    
a = Person()
a.name = "Shubham"
a.occupation = "Accountant"

b = Person()
b.name = "Mehwish"
b.occupation = "HR"
# print(a.name)
# print(a.occupation)
a.info()
b.info()