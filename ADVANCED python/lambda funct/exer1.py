def calculator(a:int, b:int, action):
    return action(a,b)

def sum(a,b):
    return a+b

def multiplication(a,b):
    return a*b

c = calculator(3, 4, lambda b,a: b**a)
print(c)