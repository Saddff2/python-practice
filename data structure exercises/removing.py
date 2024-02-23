import timeit

roll_number = [47, 64, 69, 37, 76, 83, 95, 97]
sample_dict = {'Jhon':47, 'Emma':69, 'Kelly':76, 'Jason':97}

for x in roll_number:
    if x in sample_dict:
        continue
    else:
        roll_number.remove(x)
print(roll_number)

print(timeit.timeit())