a=('1','2','pink')
b=('3','4','8')

def my_merge_tuple(a:tuple, b:tuple, is_first_loop:bool = True)->list:
    result = []
    reverse = []
    for i in a:
        for j in b:
            result.append((i,j))
    if is_first_loop:
        reverse = my_merge_tuple(b, a, is_first_loop = False)
    return result + reverse

print(my_merge_tuple(a,b))

