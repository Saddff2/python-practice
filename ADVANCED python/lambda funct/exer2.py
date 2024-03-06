my_list = [1,2,3,4,5,6,7,8,9,12,23,24]
my_dict = {'a':6, 'b':13, 4:12, 'd':17}

my_new_dict = filter(lambda a: a[1]>7, my_dict.items())

my_new = filter(lambda a:a<7, my_list)
print(dict(my_new_dict))
my_new_dict = filter(lambda a: type(a[0])==str, my_dict.items())
print(dict(my_new_dict))
