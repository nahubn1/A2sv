class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        sorted_nums = sorted(nums)
        
        result = []
        for num in nums:
            result.append(sorted_nums.index(num))
            
        return result
        
        