def check_balance(str1: str, str2:str):
    flag = True
    for x in str1:
        if x in str2:
            continue
        else: 
            flag = False
    return flag



str1 = "Yn"
str2 = "PYnative"
flag = check_balance(str1, str2)
print("it is balanced?", flag)
    
        