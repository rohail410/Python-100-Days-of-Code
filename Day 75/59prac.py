def welcomeCalculator(fx):
    def mfx(*args, **kwargs):
        print("Hello to the Calculator. Your calculation is processing.")
        fx(*args, **kwargs)
        print("Try us again.")
    return mfx

@welcomeCalculator
def sum(a, b):
    print(a + b)
    

sum(2, 3)

@welcomeCalculator
def multiply(a, b):
    print(a * b)
    
multiply(4, 2)

def divide(a, b):
    print(a / b)
    
welcomeCalculator(divide)(10, 2)

def subtract(a, b):
    print(a - b)
    
welcomeCalculator(subtract)(13, 2)