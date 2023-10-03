class TrieNode:
    def __init__(self):
        self.children = {}
        self.idx = -1
        
class WordFilter:
    def __init__(self, words: List[str]):
        self.root = TrieNode()
        for i, main_word in enumerate(words):
            for word in self.break_down(main_word):
                self.insert(word, i)
        

    
    def break_down(self, word):
        result = []
        for i in range(len(word)):
            result.append(word[i:] + '-' + word)
        
        return result

    def insert(self, word, i):
        curr = self.root
        for char in word:
            if char not in curr.children:
                curr.children[char] = TrieNode()
            
            curr = curr.children[char]
            curr.idx = i
        
    def f(self, pref: str, suff: str) -> int:
        curr = self.root
        for char in suff + '-' + pref:
            if char not in curr.children:
                return -1

            curr = curr.children[char]
        
        return curr.idx
        


# Your WordFilter object will be instantiated and called as such:
# obj = WordFilter(words)
# param_1 = obj.f(pref,suff)