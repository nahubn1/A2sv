class Solution:
    def __init__(self):
        self.mod = 10**9 + 7

    @staticmethod
    def accum(n):
        return n*(2*n-1)
    def countOrders(self, n: int) -> int:
        
        if n == 1:
            return 1
        
        return (self.accum(n)%self.mod * self.countOrders(n-1)%self.mod) % self.mod