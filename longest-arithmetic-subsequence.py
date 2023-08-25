class Solution:
    def longestArithSeqLength(self, nums: List[int]) -> int:
        dp = defaultdict(lambda:1)

        for i in range(len(nums)):
            for j in range(i):
                dp[(i, nums[i] - nums[j])] = dp[(j, nums[i] - nums[j])] + 1
        
        return max(dp.values())