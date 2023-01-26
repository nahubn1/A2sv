class Solution:
    def maxOperations(self, nums: List[int], k: int) -> int:
        nums.sort()
        opr = 0
        ptr1, ptr2= 0, len(nums)-1
        
        while ptr1 < ptr2:
            if nums[ptr1] + nums[ptr2] == k:
                opr += 1
                ptr1 += 1
                ptr2 -= 1
            
            elif nums[ptr1] + nums[ptr2] < k:
                ptr1 += 1
            else:
                ptr2 -= 1
                
        return opr