"""
Прочитати про Fibonacci search та імплементуйте його за допомогою Python.
Визначте складність алгоритму та порівняйте його з бінарним пошуком
"""

def fibonacci_search(array, value):
    n = len(array)
    f1 = 0 # Fibonacci x-2
    f2 = 1 # Fibonacci x-1
    f = f1 + f2 # Fibonacci
    while f < n:
        f2 = f1
        f1 = f
        f = f1 + f2
    offset = -1
    while f > 1:
        indx = min(offset + f2, n - 1)
        if array[indx] == value:
            return indx
        elif array[indx] > value:
            f = f2
            f1 = f1 - f2
            f2 = f - f1
        else:
            f = f1
            f1 = f2
            f2 = f - f1
            offset = indx


arr = [1, 3, 7, 15, 18, 21, 24, 31, 42, 50]
target = 24
result = fibonacci_search(arr, target)
print(f"Елемент {target} знайдено за індексом: {result}")  # Виведе: Елемент 24 знайдено за індексом: 6

"""
binary_search -> O(log n)
fibonacci_search -> O(log n)
Хоч і складність в них однакова, на практиці пошук фібоначі буде повільніше через його більш мілкий розділ частин масиву даних.
"""