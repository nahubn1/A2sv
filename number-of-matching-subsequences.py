class TrieNode:
    def __init__(self, key):
        self.val = key
        self.children = {}
        self.IsWordEnd = 0


class Trie:

    def __init__(self):
        self.root = TrieNode('*')

    def insert(self, word: str) -> None:
        last = self.root
        for char in word:
            if char not in last.children:
                last.children[char] = TrieNode(char)
            
            last = last.children[char]
        
        last.IsWordEnd += 1


class Solution:
    def numMatchingSubseq(self, s: str, words: List[str]) -> int:
        trie = Trie()
        for word in words: 
            trie.insert(word)
        
        idxes = defaultdict(list)
        idxes['*'] = [-1]
        for i, char in enumerate(s):
            idxes[char].append(i)
        
        def dfs(node, idx):
            count = 0
            i = bisect_left(idxes[node.val], idx)
            if node.val == '*' or i < len(idxes[node.val]):
                count += node.IsWordEnd
                for child in node.children:
                    count += dfs(node.children[child], idxes[node.val][i]+1)
            
            return count

        return dfs(trie.root, -1)