import timeit


n=int(input())

a = [x ** 2 for x in range(n)] #instead of  for cycle
print(a)
print(timeit.timeit())