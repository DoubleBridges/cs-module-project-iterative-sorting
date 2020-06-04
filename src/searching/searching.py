def linear_search(arr, target):
    # Your code here
    i = 0
    for _ in range(len(arr)):
        if arr[i] == target:
            return i
        i += 1
    return -1  # not found


# Write an iterative implementation of Binary Search
def binary_search(arr, target):

    # Your code here
    start = 0
    end = len(arr) - 1

    while start <= end:
        mid = int((start + end) / 2)
        if arr[mid] > target:
            end = mid - 1
        elif arr[mid] < target:
            start = mid + 1
        else:
            return mid

    return -1  # not found
