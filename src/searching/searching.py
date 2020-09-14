def linear_search(arr, target):
    # Your code here

    for i in range(0, len(arr)):
        if arr[i] == target:
            return i

        i = i+1

    return -1


# Write an iterative implementation of Binary Search
def binary_search(arr, target):

    # Your code here

    left = 0
    right = len(arr) - 1

    while left <= right:
        midpoint = (right + left) // 2
        midpoint_value = arr[midpoint]
        if midpoint_value == target:
            return midpoint
        elif midpoint_value > target:
            right = midpoint - 1
        elif midpoint_value < target:
            left = midpoint + 1

    return -1  # not found
