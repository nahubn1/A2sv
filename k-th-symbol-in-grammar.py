class Solution:
    def kthGrammar(self, n: int, k: int) -> int:
        if n == 1:
            return 0
        
        if self.kthGrammar(n-1, ceil(k/2)) == 0:
            return [1, 0][k%2]
        else:
            return [0, 1][k%2]