class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        
        memo = {}
        def dp(i, k):
           
            if (i, k) in memo:
                return memo[(i, k)]

            if i < 0:
                return k == 0

            memo[(i, k)] = dp(i-1, k+nums[i]) + dp(i-1, k-nums[i])
            
            return memo[(i, k)]
        
        return dp(len(nums)-1, target)