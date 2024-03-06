### decorator ###
def check_if(func):
    def do_it(a,b):
        a = func(a,b)
        if a <= 0:
            return None
        return a
    return do_it

def check_if2(func):
    def do_it(a,b):
        if type(a) == int and type(b) == int:
            a = func(a,b)
            if a <= 0:
                return None
            return a
        return 'a or b are not int'
    return do_it

@check_if2
def my_func(a,b):
    return a+b

###code without decorator###

def my_func2(a,b):
    return a+b

def my_func3(a,b):
    return a*b

def my_func4(a,b):
    return check_if_zero(a-b)

def check_if_zero(a):
    if a<=0:
        return None
    return a


print(my_func(13,27))
print(my_func(15,'print'))
print(my_func(1,-2))
