class Solution:
    def combinationSum4(self, nums: List[int], target: int) -> int:
        low_limit = min(nums)
        nums = set(nums)

        memo = {}
        def dp(n):
            if n in memo:
                return memo[n]

            if n < low_limit:
                return 0
            
            memo[n] = sum([dp(n-i) for i in nums]) + (n in nums)
            return memo[n]
        
        return dp(target)