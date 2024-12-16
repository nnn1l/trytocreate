"""
One way to improve the quicksort is to use an insertion sort on lists that are small in length (call it the "partition limit").
Re-implement the quicksort and use it to sort a random list of integers.
"""

import random

def quicksort_with_insertion(arr, partition_limit):
    def quicksort_recursive(arr, low, high):
        if high - low + 1 <= partition_limit:
            # Use insertion sort for small partitions
            insertion_sort_subarray(arr, low, high)
        elif low < high:
            # Partition the array
            pivot_index = partition(arr, low, high)
            # Recursively sort subarrays
            quicksort_recursive(arr, low, pivot_index - 1)
            quicksort_recursive(arr, pivot_index + 1, high)

    def partition(arr, low, high):
        pivot = arr[high]
        i = low - 1
        for j in range(low, high):
            if arr[j] < pivot:
                i += 1
                arr[i], arr[j] = arr[j], arr[i]
        arr[i + 1], arr[high] = arr[high], arr[i + 1]
        return i + 1

    def insertion_sort_subarray(arr, low, high):
        for i in range(low + 1, high + 1):
            key = arr[i]
            j = i - 1
            while j >= low and arr[j] > key:
                arr[j + 1] = arr[j]
                j -= 1
            arr[j + 1] = key

    # Start the recursive quicksort
    quicksort_recursive(arr, 0, len(arr) - 1)



# Generate a random list of integers
random_list = [random.randint(1, 100) for _ in range(20)]
print("Original list:", random_list)

# Sort the list using Quicksort with Insertion Sort optimization
partition_limit = 10  # Use insertion sort for partitions of size <= 10
quicksort_with_insertion(random_list, partition_limit)

print("Sorted list:", random_list)


