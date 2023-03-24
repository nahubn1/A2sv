class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        dup = []
        ptr = 0
        while ptr < len(nums):
            if nums[ptr]-1 == ptr or nums[ptr] == 0:
                ptr += 1
            else:
                if nums[ptr] != nums[nums[ptr]-1]:
                    nums[nums[ptr]-1], nums[ptr] = nums[ptr], nums[nums[ptr]-1]
                else:
                    dup.append(nums[ptr])
                    nums[ptr] = 0

        return dup