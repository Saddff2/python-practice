dict1 = {
    0:10,
    1:20
}

x = input('Write down first key for dictionary: ')
y = input('Write down second key for dictionary: ')

dict1[int(x)] = int(y)
print(dict1)

#-------
#exercise 2
dict1 = {'name': 'John', 'age': 25}
dict2 = {'city': 'New York', 'country': 'USA'}

newdict = {**dict1, **dict2}
print(newdict)
#-------
#exercise 3
my_dict = {'apple': 10, 'banana': 5, 'orange': 8}
x = max(my_dict.values())
print(x)
#-------
#exercise 4
keys = ['name', 'age', 'city']
values = ['John', 25, 'New York']

dict1 = dict(zip(keys, values))
print(dict1)

dict2 = dict()
for i in range(len(keys)):
    dict2.update({keys[i]: values[i]})
print(dict2)
#--------
#exercise 5
my_dict = {'name': 'John', 'age': 25, 'city': 'New York'}
x = my_dict['name']

print(x)
#--------
#exercise 6
my_dict = {'name': 'John', 'age': 25, 'city': 'New York'}
my_dict.clear()
print(my_dict)
#-------
#exercise 7
my_dict = {'name': 'John', 'age': 25, 'city': 'New York'}
for key in my_dict:
    print(key, my_dict[key])
    
#-----
#exercise 8
student = {
  'name': 'Alex',
  'class': 'V',
  'roll_id': '2'
}
key_to_check = ['name', 'building', 'roll_id']

for x in key_to_check:
    if x in student:
        print(True)
    else:
        print(False)
#------
#exercise 9
num = {'physics': 80, 'math': 90, 'chemistry': 86}
for x in list(num):
    print(x)

print('----------')
print(list(num)[0])
print(list(num)[1])
print(list(num)[2])
#------
#exercise 10
sample_dict = {
    'emp1': {'name': 'Jhon', 'salary': 7500},
    'emp2': {'name': 'Emma', 'salary': 8000},
    'emp3': {'name': 'Brad', 'salary': 500}
}
sample_dict['emp3']['salary'] = 7500
print(sample_dict)