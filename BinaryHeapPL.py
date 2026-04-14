class Heap:
    def __init__(self, size):
        self.customList = (size +1) * [None]
        self.heapSize = 0
        self.maxSize = size + 1

def heapifyTreeInsert(rootNode, index, heapType):
    parentIndex = int(index/2)
    if index<=1:
        return
    if heapType == "Min":
        if rootNode.customList[index]< rootNode.customList[parentIndex]:
            temp = rootNode.customList[index]
            rootNode.customList[index] = rootNode.customList[parentIndex]
            rootNode.customList[index] = temp
            heapifyTreeInsert(rootNode, parentIndex, heapType)
    elif heapType == "Max":
        if rootNode.customList[index]> rootNode.customList[parentIndex]:
            temp = rootNode.customList[index]
            rootNode.customList[index] = rootNode.customList[parentIndex]
            rootNode.customList[index] = temp
            heapifyTreeInsert(rootNode, parentIndex, heapType)
    
def InsertTreeNode(rootNode, NodeValue, heapType):
    if rootNode.heapSize + 1 == rootNode.maxSize:
        return "The Binary Heap is full"
    rootNode.customList[rootNode.heapSize + 1] = NodeValue
    rootNode.heapSize +=1
    heapifyTreeInsert(rootNode, rootNode.heapSize, heapType )
    return "Insert Successfull"

myHeap = Heap(7)
print(InsertTreeNode(myHeap, 1, "Min"))