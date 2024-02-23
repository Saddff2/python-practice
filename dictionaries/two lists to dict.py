keys = ['Ten', 'Twenty', 'Thirty']
values = [10, 20, 30]

dict1 = dict(zip(keys, values))
print(dict1)


dict2 = dict()
for i in range(len(keys)):
    dict2.update({keys[i]: values[i]})
print(dict2)