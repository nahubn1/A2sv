class TrieNode:
    def __init__(self, key):
        self.key = key
        self.children = {}
        self.sum = 0


class MapSum:

    def __init__(self):
        self.root = TrieNode('*')
        self.offset = defaultdict(int)

    def insert(self, key: str, val: int) -> None:
        val = val - self.offset[key]
        self.offset[key] += val

        curr = self.root
        for char in key:
            if char not in curr.children:
                curr.children[char] = TrieNode(char)
            
            curr = curr.children[char]
            curr.sum += val

    def sum(self, prefix: str) -> int:
        curr = self.root
        for char in prefix:
            if char not in curr.children:
                return 0
            
            curr = curr.children[char]

        return curr.sum

# Your MapSum object will be instantiated and called as such:
# obj = MapSum()
# obj.insert(key,val)
# param_2 = obj.sum(prefix)