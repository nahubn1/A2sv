class Solution:
    def countDistinctIntegers(self, nums: List[int]) -> int:
        nums = set(nums)
        rev_nums = set()
        
        for num in nums:
            rev = int(str(num)[::-1]) 
            if rev not in nums:
                rev_nums.add(rev)
                
        return len(nums) + len(rev_nums)