import timeit

N = 250
P = []
space = " "

for i in range(N):
    row = [1] * (i+1)
    for j in range(i+1):
        if j != 0 and j != i:
            row[j] = P[i-1][j-1]+ P[i-1][j]

    P.append(row)


for r in P:
    print(space[::-1], r)


print(timeit.timeit())