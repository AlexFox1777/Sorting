# STRETCH: implement Linear Search
from src.iterative_sorting.iterative_sorting import selection_sort


def linear_search(arr, target):
    # TO-DO: add missing code
    for num,x in enumerate(arr):
        if x == target:
            return num
    return -1  # not found


# STRETCH: write an iterative implementation of Binary Search 
def binary_search(arr, target):
    if len(arr) == 0:
        return -1  # array empty

    low = 0
    high = len(arr) - 1

    # TO-DO: add missing code
    arr = selection_sort(arr)
    print(arr)
    while(low < high):
        mid = int((high + low) / 2)
        if(target == arr[mid]):
            return mid
        if(arr[mid] < target):
            low = mid
        else:
            high = mid

    return -1  # not found

print(binary_search([-9, -8, -6, -4, -3, -2, 0, 1, 2, 3, 5, 7, 8, 9], 1))

# STRETCH: write a recursive implementation of Binary Search 
def binary_search_recursive(arr, target, low, high):
    mid = (low + high) // 2

    if len(arr) == 0:
        return -1  # array empty
    if (target == arr[mid]):
        return mid
    if (arr[mid] < target):
        return binary_search_recursive(arr, target, mid, high)
    else:
        return binary_search_recursive(arr, target, low, mid)
    # TO-DO: add missing if/else statements, recursive calls
