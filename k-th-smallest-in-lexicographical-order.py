class TrieNode:
    def __init__(self, val):
        self.val = val
        self.children = []
    def create_children(self):
        for i in range(0 if self.val else 1, 10):
            self.children.append(TrieNode(self.val*10 + i))

class Solution:
    def findKthNumber(self, n: int, k: int) -> int:
        root = TrieNode(0)

        def belowCount(num):
            if num == 0:
                return n+1
            
            mul = 1
            ans = 0
            while num*mul <= n:
                l = num*mul
                r = min(((num+1)*mul)-1, n)

                ans += r - l + 1
                mul *= 10
        
            return ans

        
        def dfs(node):           
            nonlocal i
            node.create_children()
            if i == k:
                return node.val
            if i + belowCount(node.val) <= k:
                i += belowCount(node.val)
                return
            else:
                i += 1
                for child in node.children:
                    ans =  dfs(child)
                    if ans:
                        return ans
        i = 0
        return dfs(root)