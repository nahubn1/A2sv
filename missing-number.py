class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        nums.append(-1)
        ptr = 0

        while ptr < len(nums):
            if nums[ptr] == ptr or nums[ptr] == -1:
                ptr += 1
            else:
                temp = nums[nums[ptr]] 
                nums[nums[ptr]] = nums[ptr]
                nums[ptr] = temp
          
        return nums.index(-1)