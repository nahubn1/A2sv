class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        
        nums.sort()
        diff = []
        
        for i in range(len(nums)):
            ptr1 = i+1
            ptr2 = len(nums) - 1
            while ptr1 < ptr2:
                tot = nums[i] + nums[ptr1] + nums[ptr2]
                
                diff.append([tot, abs(tot-target)])
                
                if tot < target:
                    ptr1 += 1
                elif tot > target:
                    ptr2 -= 1
                else:
                    return tot
        
        return min(diff, key= lambda item : item[1])[0]