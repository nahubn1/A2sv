class Solution:
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        n = len(nums)
        res = [-1]*n
        monStack = []
        for i in range(2*n):
            while monStack and nums[monStack[-1]] < nums[i%n]:
                res[monStack.pop()] = nums[i%n]
            else:
                monStack.append(i%n)
        
        return res