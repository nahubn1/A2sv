class Solution:
    def maxValue(self, n: int, index: int, maxSum: int) -> int:
        
        def isValid(h):

            r = min(n-index, h)
            l = min(index+1, h)

            return n + h*(r+l) - (r**2 + l**2 + r + l)/2 - (h-1) <= maxSum
            
        start, end = 1, maxSum
        while start <= end:

            middle = (start + end)//2
    
            if isValid(middle):
                start = middle + 1

            else:
                end = middle - 1
        
        return start-1