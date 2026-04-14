import QueueLinkedList as queue
class TreeNode:
    def __init__(self,data):
        self.data = data
        self.leftChild: 'TreeNode | None' = None
        self.rightChild: 'TreeNode | None' = None


newBT = TreeNode("Drinks")
leftChild = TreeNode("Hot")
rightChild = TreeNode("Cold")
newBT.leftChild = leftChild
newBT.rightChild = rightChild
tea = TreeNode("Tea")
coffee = TreeNode("coffee")
leftChild.leftChild = tea
leftChild.rightChild = coffee

def preOrderTraversal(rootNode):
    if not rootNode:
        return
    print(rootNode.data)
    preOrderTraversal(rootNode.leftChild)
    preOrderTraversal(rootNode.rightChild)

<<<<<<< HEAD
preOrderTraversal(newBT)

def inOrderTraversal(rootNode):
    if not rootNode:
        return
    inOrderTraversal(rootNode.leftChild)
    print(rootNode.data)
    inOrderTraversal(rootNode.rightChild)

inOrderTraversal(newBT)
=======

def searchBT(rootNode, nodeValue):
    if not rootNode:
        return "The BT does not exist"
    else:
        customQueue = queue.Queue()
        customQueue.enqueue(rootNode)
        while not (customQueue.isEmpty()):
            root = customQueue.dequeue()
            if root.value.data == nodeValue:
                return "Success"
            if (root.value.leftChild is not None):
                customQueue.enqueue(root.value.leftChild)
            if (root.value.rightChild is not None):
                customQueue.enqueue(root.value.rightChild)
        
        return "Not Found"
            
def insertNodeBT(rootNode, newNode):
    if not rootNode:
        rootNode = newNode
        return "Inserted Succesfully"
    else:
        customQueue = queue.Queue()
        customQueue.enqueue(rootNode)
        while not(customQueue.isEmpty()):
            root = customQueue.dequeue()
            if root.value.leftChild is not None:
                customQueue.enqueue(root.value.leftChild)
            else:
                root.value.leftChild = newNode
                return "Inserted Successfully"
            if root.value.rightChild is not None:
                customQueue.enqueue(root.value.rightChild)
            else:
                root.value.rightChild = newNode
                return "Inserted Successfully"


cola = TreeNode("Cola")

print(insertNodeBT(newBT, cola))
print(searchBT(newBT, "Cola"))
>>>>>>> ac666cf29454e1474b11cc8e1ff6f2a5ead75fca
