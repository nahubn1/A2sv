class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        if n == 1: return nums[0]
        
        memo = {}
        def dp(start, end):
            if end < start:
                return 0

            if (start, end) in memo:
                return memo[(start, end)]
            
            memo[(start, end)] = max(dp(start, end-2) + nums[end], dp(start, end-1))
            return memo[(start, end)]
        
        return max(dp(0, n-2), dp(1, n-1))