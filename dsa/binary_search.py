def binary_search(list, x):
    low = 0
    high = len(list)-1
    while (low <= high):
        mid = (low + high) // 2

        if list[mid] < x:
            low = mid + 1
        elif list[mid] > x:
            high = mid - 1
        else:
            return mid
    return -1


# Test binary search function
arr = [2, 3, 4, 10, 40]
x = 3
assert binary_search(arr, x) == 1, 'should return 1'

list = [1, 2, 3, 4, 5, 6, 7, 8, 9]
x = 1
assert binary_search(list, x) == 0, 'should return 0'

list = [4, 3,2, 1, 5,100, 20]
x = 100
list.sort()
assert binary_search(list, x) == 6, 'should return 6'
