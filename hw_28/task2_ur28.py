"""
Implement the mergeSort function without using the slice operator.
"""

def merge_sort(arr):
    if len(arr) <= 1:
        return arr

    mid_idx = len(arr) // 2
    #left_arr = arr[:mid_idx]
    #right_arr = arr[mid_idx:]
    left_arr = []
    right_arr = []
    for i in range(len(arr)):
        if i < mid_idx:
            left_arr.append(arr[i])
        else:
            right_arr.append(arr[i])


    left_arr = merge_sort(left_arr)
    right_arr = merge_sort(right_arr)

    return merge(left_arr, right_arr)






def merge(left_part, right_part):
    res = []

    while len(left_part) != 0 and len(right_part) != 0:
        if left_part[0] < right_part[0]:
            res.append(left_part[0])
            left_part.remove(left_part[0])
        else:
            res.append(right_part[0])
            right_part.remove(right_part[0])

    if len(left_part) == 0:
        res = res + right_part
    else:
        res = res + left_part
    return res

x = [50, 64, 30, 12, 100, 21, 45 ]
print(x)
y = merge_sort(x)
print(y)