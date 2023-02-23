class Solution:
    @staticmethod
    def sign(num):
        if num > 0:
            return 1
        elif num < 0:
            return -1
        else:
            return 0

    def maxTurbulenceSize(self, arr: List[int]) -> int:
        if len(arr) == 1:
            return 1
                
        stack = []
        longest = 0
        for i in range(1, len(arr)):
            
            if stack and stack[-1]*self.sign(arr[i]-arr[i-1])==-1:
                stack.append(self.sign(arr[i]-arr[i-1]))
            else:
                stack.clear()
                stack.append(self.sign(arr[i]-arr[i-1]))
            
            # print(arr[i-1], arr[i])
            # print(stack)
            
            longest = max(longest, len(stack)*abs(stack[0]) + 1)
            # print('>', longest)
        
        return longest