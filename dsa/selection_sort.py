arr = [2, 3, 5, 6, 100, 1]

# write a function that finds the smallest element of an array
def find_smallest(arr):
    smallest = arr[0]
    smallest_index = 0
    for i in range(1, len(arr)):
        if arr[i] < smallest:
            smallest = arr[i]
            smallest_index = i
    return smallest_index
assert find_smallest(arr) == 5   

# write a function that orders array elements from smallest to largest, and place the elements into a new array. (selection sort)
# use .pop(index) to remove an element from an array
def selection_sort(arr):
    newArr = []
    for i in range(len(arr)):
      smallest = find_smallest(arr) # we have the smallest index
      newArr.append(arr.pop(smallest))
    return newArr # ordered from smallest to largest
  
assert selection_sort(arr) == [1, 2, 3, 5, 6, 100]
