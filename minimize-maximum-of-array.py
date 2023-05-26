class Solution:
    def minimizeArrayValue(self, nums: List[int]) -> int:
        ans = nums[0]
        rSum = nums[0]

        for i in range(1, len(nums)):
            rSum += nums[i]
            ans = max(ans, ceil(rSum/(i+1)))
        
        return ans