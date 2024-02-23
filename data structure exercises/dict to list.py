speed = {'jan': 47, 'feb': 52, 'march': 47, 'April': 44, 'May': 52, 'June': 53, 'july': 54, 'Aug': 44, 'Sept': 54}
slist1 = []

for x in speed.values():
    if x in slist1:
        continue
    else:
        slist1.append(x)

print(slist1)