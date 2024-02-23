first_set = {23, 42, 65, 57, 78, 83, 29}
second_set = {57, 83, 29, 67, 73, 43, 48}

x = first_set.intersection(second_set)

print(x)
for item in x:
    first_set.remove(item)

print(first_set)