def swap(myList, i, j):
    myList[i], myList[j] = myList[j], myList[i]

def pivot(myList,pivot_index, end_index):
    swap_index = pivot_index
    for i in range(pivot_index+1, end_index+1):
        if myList[i] < myList[pivot_index]:
            swap_index += 1
            swap(myList, swap_index, i)
    swap(myList, pivot_index, swap_index)
    return swap_index

def quickSort_helper(myList, left, right):
    if left < right:
        pivot_index = pivot(myList, left, right)
        quickSort_helper(myList, left, pivot_index-1)
        quickSort_helper(myList, pivot_index+1, right)
    return myList

def quickSort(myList):
    return quickSort_helper(myList, 0, len(myList)-1)

myList = [4, 2, 6, 5, 1, 3]
print(quickSort(myList))