
num = 0
x = 1
y = 1
while x < 2000000:
    z = x + y
    x = z + y
    y = x + z
    if x % 2 == 0:
        num += x
    elif y % 2 == 0:
        num += y
    elif z % 2 == 0:
        num += z
    else:
        pass
print(num)
