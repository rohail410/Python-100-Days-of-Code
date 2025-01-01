class Employee:
    # Contructor
    def __init__(self, name, age, role):
        self.name = name
        self.age = age
        self.role = role
        

    # Alternative Constructor
    @classmethod
    def fromHyphen(cls, entry):
        formatted = entry.split("-")
        return cls(formatted[0], int(formatted[1]), formatted[2])
            
    @classmethod
    def fromUnderscore(cls, entry):
        formatted = entry.split("_")
        return cls(formatted[0], formatted[1], formatted[2])

    @classmethod
    def fromSpaces(cls, entry):
        formatted = entry.split(" ")
        return cls(formatted[0], formatted[1], formatted[2])
    
    # Instance Methods
    def show(self):
        print(f"The Employee name is {self.name} and age is {self.age} and his role is {self.role}.")
    

e1 = Employee("Rohail", 23, "Developer") 
e1.show()

e2 = Employee.fromHyphen("Junaid-28-Junior Manager")
e2.show()

e3 = Employee.fromUnderscore("Haddiya_32_Student")
e3.show()

e4 = Employee.fromSpaces("Ayaan 43 CEO")
e4.show()

# format1 = "Zain-35-HR"
# formatted1 = format1.split("-")
# print(formatted1)
# e2 = Employee(format1.split("-")[0], format1.split("-")[1],  format1.split("-")[2])

# e2.show()

# e3 = Employee(formatted1[0], formatted1[1], formatted1[2])
# e3.show()
