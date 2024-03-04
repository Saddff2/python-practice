x = 1000
i=0
for x in range(900, 1000):
    for y in range(900, 1000):
        num = str(x*y)
        if num == num[::-1]:
            ans = num
            print(ans)
        else:
            pass
print(ans)