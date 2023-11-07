class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        nums = sorted([(nums[i], i) for i in range(len(nums))])
        ptr1 = 0
        ptr2 = len(nums)-1
        
        while ptr1 < ptr2:
            if nums[ptr1][0] + nums[ptr2][0] == target:
                return [nums[ptr1][1], nums[ptr2][1]]
            elif nums[ptr1][0] + nums[ptr2][0] > target:
                ptr2 -= 1
            else:
                ptr1 += 1
        
    
