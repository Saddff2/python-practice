#Write a Python program to create a calculator class.
#Include methods for basic arithmetic operations.

class Calculator:
    def __init__(self):
        pass
    
    def get_sum(self, x, y):
        print(f'{x} + {y} = ',x + y)
        return x + y
    
    def get_substract(self, x, y):
        print(f'{x} - {y} = ', x - y)
        return x - y
    
    def get_multiply(self, x, y):
        print(f'{x} * {y} = ', x * y)
        return x * y
    
    def get_divide(self, x, y):
        if x != 0:
            print(f'{x} / {y} = ', x / y)
            return x / y
        else:
            ("Can't divide by zero")
    
calculator = Calculator()


calculator.get_sum(10,20)

calculator.get_divide(10000, 100)