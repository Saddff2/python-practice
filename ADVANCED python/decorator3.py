def decorator(func):
    def wrapper(arr):
        filtered_array = [i for i in arr if isinstance(i,int)]
        return func(filtered_array)
    return wrapper

@decorator
def calc_avg(arr):
    if not arr:
        return 0
    return f'average is {sum(arr)/len(arr)}, sum is {sum(arr)} of list of numbers {len(arr)}'

arr = [1,2,'a',4,5,10,25,4000,105]

print(calc_avg(arr))

