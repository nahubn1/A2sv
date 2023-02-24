from math import inf
class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        s, winSum, minLen = 0, 0, inf
        for e in range(len(nums)):
            winSum += nums[e]
            while winSum >= target:
                minLen = min(minLen, e-s+1)
                winSum -= nums[s]
                s += 1
        return minLen if minLen<inf else 0