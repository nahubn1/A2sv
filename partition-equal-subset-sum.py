class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        total = sum(nums)
        if total % 2 == 1: return False

        @cache
        def dp(i, k):
            if k < 0:
                return False

            if i == len(nums):
                return k == 0

            return dp(i+1, k) or dp(i+1, k-nums[i])
        
        return dp(0, total//2)