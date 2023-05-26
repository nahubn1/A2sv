class Solution:
    def minDifference(self, nums: List[int]) -> int:
        if len(nums) < 4:
            return 0
        
        nums.sort()
        ans = inf
        for i in range(4):
            ans = min(ans, nums[i-4] - nums[i])
        
        return ans