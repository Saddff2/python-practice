import timeit


n=int(input())

a = [x ** 2 for x in range(n)] #вместо цикла for
print(a)
print(timeit.timeit())