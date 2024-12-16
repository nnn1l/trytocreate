"""
A bubble sort can be modified to "bubble" in both directions.
The first pass moves "up" the list and the second pass moves "down."
This alternating pattern continues until no more passes are necessary.
Implement this variation.
"""


def bidirectional_bubble_sort(array):
    const_max = len(array) - 1
    it_er, indx, up = 0, 0, True
    while it_er <= const_max:
        if up is True:
            print('UP')
            for i in range(const_max - it_er):
                print(indx)
                if array[indx] > array[indx + 1]:
                    temp = array[indx + 1]
                    array[indx], array[indx + 1] = array[indx + 1], array[indx]
                    array[indx] = temp
                indx += 1
            it_er += 1
            up = False

        else:
            print('DOWN')
            for i in range(const_max - it_er):
                print(indx)
                if array[indx] < array[indx - 1]:
                    temp = array[indx - 1]
                    array[indx], array[indx - 1] = array[indx - 1], array[indx]
                    array[indx] = temp
                indx -= 1
            it_er += 1
            up = True
    return array


test_list = [22, 6, 41, 10, 47, 20, 24, 49, 37, 34, 15]
test_list_copy = test_list.copy()
test_list_copy = bidirectional_bubble_sort(test_list_copy)
print(test_list, '\n', test_list_copy)
"""
[22, 6, 41, 10, 47, 20, 24, 49, 37, 34, 15] 
[6, 10, 15, 20, 22, 24, 34, 37, 41, 47, 49]
"""