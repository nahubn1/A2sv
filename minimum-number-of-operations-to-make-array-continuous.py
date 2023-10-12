class Solution:
    def minOperations(self, nums: List[int]) -> int:
        n = len(nums)
        nums = sorted(set(nums))

        ans = inf
        for i in range(len(nums)):
            left = nums[i]
            right = left + (n-1)

            j = bisect_right(nums, right)

            ans = min(ans, n - (j-i))
        
        return ans