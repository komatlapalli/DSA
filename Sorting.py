#BubbleSort

def bubbleSort(customList):
    for i in range(len(customList)-1):
        for j in range(len(customList)-i-1):
            if customList[j]> customList[j+1]:
                temp = customList[j]
                customList[j] = customList[j+1]
                customList[j+1] = temp

    print(customList)

def selectionSort(customList):
    for i in range(len(customList)):
        min_index = i
        for j in range(i+1, len(customList)):
            if customList[min_index] > customList[j]:
                min_index = j
        customList[i], customList[min_index] = customList[min_index], customList[i]
    print(customList)

def insertionSort(customList):
    for i in range(1, len(customList)):
        key = customList[i]
        j = i-1
        while j>=0 and key < customList[j]:
            customList[j], customList[j+1] = key,customList[j]
            j-=1
    print(customList)

            


customList = [1,9,8,5,2,4,3]
print(customList)
insertionSort(customList)