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


newTrie = Trie()
newTrie.insert("apple")
print(newTrie.root.children)
print(newTrie.root.children['a'].children)
print(newTrie.root.children['a'].children['p'].children)  # Output: {'a': <__main__.TrieNode object at 0x...>   }
print(newTrie.root.children['a'].children['p'].children['p'].children)  # Output: {'l': <__main__.TrieNode object at 0x...>   }
print(newTrie.root.children['a'].children['p'].children['p'].children['l'].children)  # Output: {'e': <__main__.TrieNode object at 0x...>   }
print(newTrie.root.children['a'].children['p'].children['p'].children['l'].children['e'].endOfString)  # Output: True                           