import timeit


def digitsinstring(str1):
    sum = 0
    count = 0
    for x in str1:
        if x.isdigit():
            sum += int(x)
            count += 1
    print(sum, sum/count)

digitsinstring("PYnative29@#8496")

print(timeit.timeit())

        