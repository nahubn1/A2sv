class Solution:
    def pow(self, x, n):
        if n == 0:
            return 1
        elif n == 1:
            return x
        else:
            if n%2 == 0:
                return self.pow(x*x, n/2)
            else:
                return x*self.pow(x*x, (n-1)/2)

    def myPow(self, x: float, n: int) -> float:
        if n < 0:
            n = -n
            x = 1/x
        
        return self.pow(x, n)