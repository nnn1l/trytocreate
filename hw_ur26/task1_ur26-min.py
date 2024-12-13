"""
Реалізувати алгоритм бінарного пошуку за допомогою рекурсії.
"""

def binary_search(array, value, right, left=0):
    if right < left:
        return -1
    mid = left + (right - left) // 2
    if len(array) == 1:
        return 0
    if array[mid] == value:
        return mid
    if array[mid] < value:
        return binary_search(array, value, right, mid + 1)
    if array[mid] > value:
        return binary_search(array, value, mid - 1, left)


l = [1,3,5,7,9]
assert binary_search(l, 9, len(l) - 1) == 4
assert binary_search(l, 8, len(l) - 1) == -1