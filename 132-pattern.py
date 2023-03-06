class Solution:
    def find132pattern(self, nums: List[int]) -> bool:
        n = len(nums)        
        minStack = [nums[0]]
        for i in range(1, n): 
            minStack.append(min(minStack[-1], nums[i]))

        monStack = []
        for j in range(n-1, -1, -1):
            while monStack and monStack[-1] < nums[j]:
                nums_k = monStack.pop()
                nums_i = minStack[j]

                if nums_i < nums_k < nums[j]:
                    return True
            monStack.append(nums[j])
        return False