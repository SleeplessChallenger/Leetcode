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

# 2. medium - Design Add and Search Words Data Structure
class WordDictionary:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.root = {}
        self.Symbol = '*'
    
    # trie
    def addWord(self, word: str) -> None:
        node = self.root
        for letter in word:
            if letter not in node:
                node[letter] = {}
            node = node[letter]
        node[self.Symbol] = '*'
        

    def search(self, word: str, node=None) -> bool:
        node = self.root
        def search_inner(word, node):
            
            for idx in range(len(word)):
                letter = word[idx]
                # if '.' is met: explore all letters
                if letter == '.':
                    for i in node:
                        # [a] - add; [a.] - search => False
                        # if we remove `i != '*'` then we won't
                        # catch this case as we have end, but `.`
                        # still wants to search further
                        if i != '*' and search_inner(word[idx + 1:], node[i]):
                            return True
                if letter not in node:
                    return False
                node = node[letter]
        
            return self.Symbol in node
        
        return search_inner(word, node)
