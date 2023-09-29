class TrieNode:
    def __init__(self, key, parent=None):
        self.key = key
        self.parent = parent
        self.children = {}
        self.isWordEnd = False

class Tire:
    def __init__(self):
        self.root = TrieNode('*')
        self.root.isWordEnd = True
    
    def insert(self, word: str) -> None:
        curr = self.root
        for char in word:
            if char not in curr.children:
                curr.children[char] = TrieNode(char, curr)
            
            curr = curr.children[char]
        
        if curr.parent.isWordEnd:
            curr.isWordEnd = True

        return curr

class Solution:
    def longestWord(self, words: List[str]) -> str:
        words.sort()
        tire = Tire()
        ans = (0, '')

        for word in words:
            leaf = tire.insert(word)
            if leaf.isWordEnd:
                ans = min(ans, (-len(word), word))

        return ans[1]