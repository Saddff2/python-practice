sample_list = [11, 45, 8, 11, 23, 45, 23, 45, 89]
count_dict = dict()
for x in sample_list:
    if x in count_dict:
        count_dict[x] += 1
    else:
        count_dict[x] = 1
print(count_dict)