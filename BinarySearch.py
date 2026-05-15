import math

def binarySearch(arr, target):
    start = 0
    end = len(arr) - 1
    mid = math.floor((start + end) / 2)
    while not arr[mid] == target and start <= end:
        if target < arr[mid]:
            end = mid - 1
        else:
            start = mid + 1
        mid = math.floor((start + end) / 2)

    if arr[mid] == target:
        return mid
    else:
        return -1
        
        
myList = [1, 2, 3, 4, 5, 6, 7, 8, 9]
print(binarySearch(myList, 10))