def binary_search(list1, target):
    left = 0
    right = len(list1) - 1

    while left <= right:
        mid = (left + right) // 2
        if list1[mid] == target:
            return mid
        elif list1[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    
    return -1


list1 = [1,2,3,5,3,2,4,5,6,2,5,1,3,5,6,3,7,7,8,9,9,3,5,3,3333,5,5,5,5,6,7,8,8,4,62,6,3,6,4,6,4,6,3,5,2,6,7,7,7,45,3,25555,3,3,2,2,2,2,2,2,2]
x = sorted(list1)
print(x)
print(binary_search(x, 25555))