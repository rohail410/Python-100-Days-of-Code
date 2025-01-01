class Employee:
    companyName = "SadaPay"
    
    def __init__(self, name):
        self.name = name
        self.r_amount = 0.02
        
    def showInfo(self):
        print(f"Employee name is {self.name} and has a raise amount of {self.r_amount}% in company {self.companyName}.")
        
    
e1 = Employee("Rohail")
# Employee.showInfo(e1, "Google")
e1.showInfo()

e2 = Employee("Inam")
e2.r_amount = 0.3
e2.companyName = "Ali Baba"
e2.showInfo()