

def check_if(from_what):
    def function(func):
        def do_it(*args):
            for i in list(args):
                if type(i) != int:
                    return 'not int'
            result =  func(*args)
            if result is not None and result <= from_what:
                return None
            return result
        return do_it
    return function


@check_if(2)
def my_func(*args):
    return sum(args)


print(my_func(1,2))