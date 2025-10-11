class Node:
    def __init__(self,value) -> None:
        self.value = value
        self.next = None
class Linkedlist:
    def __init__(self):
        self.head = None
        self.tail = None
        self.length = 0

    def __str__(self) -> str:
        temp_node = self.head
        result = ''
        while temp_node is not None:
            result += str(temp_node.value)
            if temp_node.next is not None:
                result += ' -> '
            temp_node = temp_node.next
        return result
    
    def prepend(self,value):
        new_node = Node(value)
        if self.head == None:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.next = self.head
            self.head = new_node

        self.length += 1
    def append(self,value):
        new_node = Node(value)
        if self.head == None:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node
        self.length +=1

    def insert(self,index,value):
        if index < 0 or index > self.length:
            return False
        if index == 0:
            self.prepend(value)
            return True
        if index == self.length:
            self.append(value)
            return True
        
        new_node = Node(value)
        temp_node = self.head
        for _ in range(index - 1):
            temp_node = temp_node.next
        new_node.next = temp_node.next
        temp_node.next = new_node
        self.length += 1
        return True
    
    def search(self,value):
        temp_node = self.head
        while temp_node is not None:
            if temp_node.value == value:
                return True
            temp_node = temp_node.next
        return False
    def get(self,index):
        if index < 0 or index >= self.length:
            return None
        temp_node = self.head
        for _ in range(index):
            temp_node = temp_node.next
        return temp_node.value
    
    def set(self,index,value):
        if index < 0 or index >= self.length:
            return False
        temp_node = self.head
        for _ in range(index):
            temp_node = temp_node.next
        temp_node.value = value
        return True
    def pop_first(self):
        if self.length == 0:
            return None
        temp_node = self.head
        self.head = self.head.next
        temp_node.next = None
        self.length -= 1
        if self.length == 0:
            self.tail = None
        return temp_node.value
    
    def traverse(self):
        temp_node = self.head
        while temp_node is not None:
            print(temp_node.value)
            temp_node = temp_node.next

    def remove(self,index):
        if index < 0 or index >= self.length:
            return None
        if index == 0:
            return self.pop_first()
        temp_node = self.head
        for _ in range(index - 1):
            temp_node = temp_node.next
        removed_node = temp_node.next
        temp_node.next = removed_node.next
        removed_node.next = None
        self.length -= 1
        if index == self.length:
            self.tail = temp_node
        return removed_node.value

    
    