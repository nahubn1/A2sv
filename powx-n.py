class Solution:
    def myPow(self, x: float, n: int) -> float:
        postive = True if n > 0 else False
        n = abs(n)

        res = 1
        base = x
        for i in range(n.bit_length()):
            if n & (1 << i) != 0:
                res *= base
            
            base *= base
        
        return res if postive else 1/res