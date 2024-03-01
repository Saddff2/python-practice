import re

line = "my age is 24 and I have 3 children and I have 1000 friend and 89"
m = re.search(r'(\d+).*', line)
#if m:
#    print("matched string is {} in index ({}, {})".format(
#        m.group(1), m.start(1), m.end(1)))
#else:
#    print('no match')

m1 = re.search(r'\d', line)
m = re.search(r'\d+', line)
n = re.search(r'\d.*', line)
o = re.findall(r'\d+', line)

print('m1', m1)
print('m',m )
print('n', n)
print('o', o)