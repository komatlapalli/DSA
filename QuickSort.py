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

