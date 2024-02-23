my_list = [1,2,3,5,[1,2,(1,2,3),3],[5,7,8,[6,6,5],9,10]]

def my_list_sum(my_list:list)->int:
    i=0
    for j in my_list:
        my_type = type(j)
        if my_type == list or my_type == tuple:
            i += my_list_sum(j)
        else:
            i += j
    return i



second_list = [1,2,11,[15,5,6], 7]

def second_list_sum(second_list: list)->int:
    total=0 
    for x in second_list:
        if type(x) == int:
            total += x
            print(total)
        else:
            for y in x:
                total += y
                if total >= 21:
                   return 'BOOM'
                print(total)
        if total >= 21:
            return 'BOOM'
    return total



print(second_list_sum(second_list))