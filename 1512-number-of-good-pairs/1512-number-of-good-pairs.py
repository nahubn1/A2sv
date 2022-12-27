from math import comb
class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        hashmap = {}
        for i in nums:
            if i in hashmap:
                hashmap[i] += 1
            else:
                hashmap[i] = 1
        
        pairs = 0       
        for i in hashmap.values():
            pairs += comb(i,2)
            
        return pairs