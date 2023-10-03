class Solution:
    def maxScore(self, nums: List[int]) -> int:

        @cache
        def dp(mul, visited):
            if mul > len(nums)//2:
                return 0
        
            ans = 0
            for i in range(len(nums)):
                for j in range(i+1, len(nums)):
                    if visited & (1<<i) or visited & (1<<j):
                        continue
                    
                    ans = max(ans, mul*gcd(nums[i], nums[j]) + dp(mul+1, visited |(1<<i) | (1<<j)))
            
            return ans
        
        return dp(1, 0)