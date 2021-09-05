# 1. Index Pairs of a String
class Solution:
    '''
    We use Trie (not Suffix Trie) to store
    all words. We'll have like:
    
        root
        /   \
      'a'   'a'
       |     |
      'b'   'b'
       |     |
      '*'   'a'
             |
            '*'
    Then we start traversing the `text`. Use helper
    funcition to proceed with current idx (it will denote
    the start position in the big string). In helper start
    exploring big string again and if letter not found in
    trie -> break. Else, move to the next letter. If '*' is found
    => end of the string, hence add to result. BUT!!! don't break
    from function and continue iteration as we can find next
    string. I.e. at first we found 'ab' and then 'aba'.
    '''
    def indexPairs(self, text: str, words: List[str]) -> List[List[int]]:
        trie = Trie()
        for word in words:
            trie.insert(word)
    
        result = []
        for idx in range(len(text)):
            self.traverse(idx, text, trie, result)
            
        return result
    
    def traverse(self, idx, text, trie, result):
        nodes = trie.root
        for i in range(idx, len(text)):
            letter = text[i]
            if letter not in nodes:
                return False
            nodes = nodes[letter]
            if '*' in nodes:
                result.append([idx, i])
                

class Trie:
    def __init__(self):
        self.root = {}
        
    def insert(self, word):
        node = self.root
        for letter in word:
            if letter not in node:
                node[letter] = {}
            node = node[letter]
        node['*'] = True
