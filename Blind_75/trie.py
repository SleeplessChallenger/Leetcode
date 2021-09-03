# medium chunk
# 1. medium - Implement Trie (Prefix Tree)
class Trie:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.root = {}
        self.endSymbol = '*'
        

    def insert(self, word: str) -> None:
        """
        Inserts a word into the trie.
        """
        node = self.root
        for letter in word:
            if letter not in node:
                node[letter] = {}
            node = node[letter]
        
        node[self.endSymbol] = True
        
    
    def search(self, word: str) -> bool:
        """
        Returns if the word is in the trie.
        """
        node = self.root
        for letter in word:
            if letter not in node:
                return False
            
            node = node[letter]
        
        # to check that actual word in the ht
        return self.endSymbol in node

    def startsWith(self, prefix: str) -> bool:
        """
        Returns if there is any word in the trie that starts with the given prefix.
        """
        node = self.root
        for letter in prefix:
            if letter not in node:
                return False
            node = node[letter]
        
        return True
