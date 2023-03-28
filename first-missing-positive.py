class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:        
        for i in range(len(nums)):
            while nums[i] != 0 and nums[i]-1 != i:
                if not( 0 < nums[i] <= len(nums)) or nums[i] == nums[nums[i]-1]:
                    nums[i] = 0
                else:
                    if nums[i] > len(nums):
                        nums[i] = -1
                    else:
                        nums[nums[i]-1], nums[i] = nums[i], nums[nums[i]-1]
                
        ptr = 0
        while ptr < len(nums):
            if nums[ptr] == 0:
                break
                
            ptr += 1

        return ptr+1