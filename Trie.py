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



newTrie = Trie()
newTrie.insert("apple")
newTrie.insert("app")
print(newTrie.search("apple"))  # Output: True
print(newTrie.search("app"))    # Output: True
print(newTrie.search("ap"))     # Output: False
                         