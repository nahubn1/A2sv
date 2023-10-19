class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        if not nums:
            return True
            
        memo = {}
        def dp(i, k):

            if (i, k) in memo:
                return memo[(i, k)]
            
            if k < 0 or i < 0:
                return k == 0

            memo[(i, k)] =  dp(i-1, k) or dp(i-1, k - nums[i])
            return memo[(i, k)]
        
        return dp(len(nums)-1, sum(nums)/2)