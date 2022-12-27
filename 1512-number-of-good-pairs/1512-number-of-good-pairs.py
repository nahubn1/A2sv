from math import comb
from collections import Counter
class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        count = Counter(nums)
        pairs = 0       
        for i in count.values():
            pairs += comb(i,2)
            
        return pairs