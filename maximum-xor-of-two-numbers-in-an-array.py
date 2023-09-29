# class TrieNode:
#     def __init__(self, key):
#         self.key = key
#         self.children = {}


class Trie:

    def __init__(self, bit_len):
        self.root = {}
        self.bit_len = bit_len

    def insert(self, num: str) -> None:
        curr = self.root
        for i in range(self.bit_len, -1, -1):
            bit = 1 if num & (1<<i) else 0 
            if bit not in curr:
                curr[bit] = {}
            
            curr = curr[bit]
    
    def maxXOR(self, num):
        ans = 0
        curr = self.root
        for i in range(self.bit_len, -1, -1):
            bit = 1 if num & (1<<i) else 0 
            if bit^1 in curr:
                ans |= (1<<i)
                curr = curr[bit^1]
            else:
                curr = curr[bit] 
        
        return ans

class Solution:
    def findMaximumXOR(self, nums: List[int]) -> int:
        trie = Trie(max(nums).bit_length())
        for num in nums:
            trie.insert(num)
        
        ans = 0
        for num in nums:
            ans = max(ans, trie.maxXOR(num))
        
        return ans