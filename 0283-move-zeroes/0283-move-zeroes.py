class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        ptr1 = 0
        ptr2 = len(nums) - 1
        
        while ptr1 < ptr2:
            if nums[ptr1] == 0:
                nums.append(0)
                nums.pop(ptr1)
                ptr2 -= 1
            else:
                ptr1 += 1