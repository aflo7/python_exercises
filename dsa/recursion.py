#write a function to calculate the factorial of a number
# 5 = 5 *4*3*2*1
def fact(num):
  if (num == 1):
    return 1
  else:
    return (num * fact(num-1))
print(fact(3))

# you're given an array of numbers. create a function to return the sum of all the numbers in the array.
# arr = [1, 2, 3]
# def sum(arr): 
#   total = 0
#   for x in arr:
#     total += x 
#   return total

# assert sum(arr) == 6

# # now write the same function recursively
# arr2 = [20, 1, 2, 3]
# def recursiveSum(arr):
#     if (len(arr) == 1):
#       return arr[0]
#     else:
#       return arr.pop(0) + recursiveSum(arr)
# assert recursiveSum(arr2) == 26