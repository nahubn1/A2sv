class Solution:
    def maxSubarrays(self, nums: List[int]) -> int:
        n = len(nums)
        guess = 1
        window = 2097151
        for i in range(n):
            window = window & nums[i]

            if window == 0 and i != n-1:
        
                guess += 1
                window = 2097151

        return guess if window == 0 else 1 if guess == 1 else guess - 1