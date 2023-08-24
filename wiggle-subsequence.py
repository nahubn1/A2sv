class Solution:
    def wiggleMaxLength(self, nums: List[int]) -> int:
        n = len(nums)
        dp = {(n-1, 1): 1, (n-1, -1): 1}

        for i in range(len(nums)-2, -1, -1):
            for sign in [1, -1]:
                leave = dp[(i+1, sign)]
                take = 0
                if sign * (nums[i] - nums[i+1]) > 0:
                    take = 1 + dp[(i+1, -1 * sign)]

                dp[(i, sign)] = max(leave, take)

        
        return max(dp[(0, 1)], dp[(0, -1)])