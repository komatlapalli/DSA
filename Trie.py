class TrieNode:
    def __init__(self):
        self.children = {}
        self.endOfString = False

class Trie:
    def __init__(self):
        self.root = TrieNode()


newTrie = Trie()
print(newTrie.root.children)  # Output: {}
print(newTrie.root.endOfString)  # Output: False