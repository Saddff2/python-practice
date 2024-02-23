l1 = [3, 6, 9, 12, 15, 18, 21]
l2 = [4, 8, 12, 16, 20, 24, 28]
ans = list()

odd_elements = l1[1::2]
print(odd_elements)
even_elements = l2[0::2]
print(even_elements)

x = odd_elements + even_elements
ans = sorted(x)
print(x)