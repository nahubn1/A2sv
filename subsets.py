class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        subsets = []

        def backtack(start, arr):
            subsets.append(arr)
            for i in range(start, len(nums)):
                backtack(i+1, arr+[nums[i]])
        
        backtack(0, [])

        return subsets