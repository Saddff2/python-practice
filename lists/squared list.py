numbers = [1, 2, 3, 4, 5, 6, 7]

square_list = []                # for loop
for x in numbers:
    square_list.append(x**2)
print(square_list)

res = [x * x for x in numbers] #list comprehension
print("comprehensed list: " + str(res))