from itertools import accumulate
class Solution:
    def maxSumRangeQuery(self, nums: List[int], requests: List[List[int]]) -> int:
        n = len(nums)

        overlap = [0]*n
        for l, r in requests:
            overlap[l] += 1
            if r < n-1: overlap[r+1] -= 1
                
        overlap = list(accumulate(overlap))

        overlap.sort()
        nums.sort()

        max_req = 0
        for i, j in zip(overlap, nums):
            max_req += (i*j)
        
        return max_req % (10**9 + 7)
        