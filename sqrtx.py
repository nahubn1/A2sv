class Solution:
    def mySqrt(self, x: int) -> int:
        if x == 0:
            return 0
            
        start = 1
        end = x
        while start <= end:
            middle = (start+end)//2
            if middle*middle < x:
                start = middle + 1
            elif middle*middle > x:
                end = middle - 1
            else:
                return middle
        
        return middle if middle*middle <= x else middle-1