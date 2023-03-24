class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        i = 0
        while i < len(nums):
            if i == nums[i]-1:
                i += 1
            else:
                if nums[i] != nums[nums[i]-1]:
                    nums[nums[i]-1], nums[i] = nums[i], nums[nums[i]-1]
                else:
                    return nums[i]