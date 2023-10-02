class TrieNode:
    def __init__(self):
        self.children = {}
        self.prefixSum = 0

class Trie:
    def __init__(self):
        self.root = TrieNode()
    
    def insert(self, word):
        curr = self.root
        for char in word:
            if char not in curr.children:
                curr.children[char] = TrieNode()
            
            curr = curr.children[char]
            curr.prefixSum += 1
    
    def find(self, word):
        ans = 0
        curr = self.root

        for char in word:
            if char not in curr.children:
                curr.children[char] = TrieNode()
            
            curr = curr.children[char]
            ans += curr.prefixSum 
        
        return ans

class Solution:
    def sumPrefixScores(self, words: List[str]) -> List[int]:
        trie = Trie()
        
        for word in words: 
            trie.insert(word)

        ans = []
        for word in words:
            ans.append(trie.find(word))
        
        return ans