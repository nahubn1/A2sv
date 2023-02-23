class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prefix_mul = []
        mul = 1
        for i in nums:
            mul *= i
            prefix_mul.append(mul)
                
        postfix_mul = []
        mul = 1
        for i in reversed(nums):
            mul *= i
            postfix_mul.insert(0, mul)
        
        output = []
        for i in range(len(nums)):
            if i == 0:
                output.append(postfix_mul[i+1])
            elif i == len(nums)-1:
                output.append(prefix_mul[i-1])
            else:
                output.append(prefix_mul[i-1]*postfix_mul[i+1])
        
        return output