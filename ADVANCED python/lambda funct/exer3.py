my_list = [1,2,3,4,5,6,7,8,9,12,23,24]

a = map(lambda a:a + 12 if a > 7 else a, my_list)
print(list(a))
a = map(lambda a:a + 12, filter(lambda a: a>7, my_list))
print(list(a))

my_list1 = [1,2,3,4,5,6,7,8,9,12,23,24]
my_list2 = [1,2,3,4,5,6,7,8,9,12,23,24]