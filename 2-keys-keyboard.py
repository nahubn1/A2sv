class Solution:
    def minSteps(self, n: int) -> int:
        
        @cache
        def dp(count, copy):
            if count == n:
                return 0

            if count > n:
                return inf

            return min(2+dp(2*count, count), 1+dp(count+copy, copy) if copy else inf)  
       
        return dp(1, 0)