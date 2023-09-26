class TrieNode:
    def __init__(self, key):
        self.children = {}
        self.IsWordEnd = False

class WordDictionary:

    def __init__(self):
        self.root = TrieNode('*')

    def addWord(self, word: str) -> None:
        last = self.root
        for char in word:
            if char not in last.children:
                last.children[char] = TrieNode(char)
            
            last = last.children[char]
        
        last.IsWordEnd = True

    def search(self, word: str) -> bool:
        que = deque([self.root])
        for char in word:
            for _ in range(len(que)):
                node = que.popleft()
                if char == '.':
                    que.extend(node.children.values())
                elif char in node.children:
                    que.append(node.children[char])
            
            if not que: return False
                

        return any([node.IsWordEnd for node in que])
        


# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)