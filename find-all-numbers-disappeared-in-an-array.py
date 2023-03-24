class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        ptr = 0
        while ptr < len(nums):
            if nums[ptr]-1 == ptr or nums[ptr] == 0:
                ptr += 1
            else:
                if nums[ptr] != nums[nums[ptr]-1]:
                    temp = nums[ptr]
                    nums[ptr] = nums[nums[ptr]-1]
                    nums[temp-1] = temp
                else:
                    nums[ptr] = 0

        return [i+1 for i in range(len(nums)) if nums[i] == 0]