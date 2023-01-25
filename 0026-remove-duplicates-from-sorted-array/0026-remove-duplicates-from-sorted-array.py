class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        
        i = 1
        f = len(nums)
        while i < f:
            if nums[i] == nums[i-1]:
                nums.pop(i)
                f -= 1
            else:
                i += 1

                