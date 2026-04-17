class TrieNode:
    def __init__(self):
        self.children = {}
        self.endOfString = False

class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word):
        currentNode = self.root
        for char in word:
            if char not in currentNode.children:
                currentNode.children[char] = TrieNode()
            currentNode = currentNode.children[char]
        currentNode.endOfString = True

    def search(self, word):
        currentNode = self.root
        for char in word:
            if char not in currentNode.children:
                return False
            currentNode = currentNode.children[char]
        return currentNode.endOfString
    

def deleteString(node, word, index):
    if index == len(word):
        if not node.endOfString:
            return False
        node.endOfString = False
        return len(node.children) == 0

    char = word[index]
    if char not in node.children:
        return False

    shouldDeleteCurrentNode = deleteString(node.children[char], word, index + 1)

    if shouldDeleteCurrentNode:
        del node.children[char]
        return len(node.children) == 0 and not node.endOfString

    return False    




newTrie = Trie()
newTrie.insert("apple")
newTrie.insert("app")
print(deleteString(newTrie.root, "app", 0))
print(newTrie.search("app"))
print(newTrie.search("apple"))
                         