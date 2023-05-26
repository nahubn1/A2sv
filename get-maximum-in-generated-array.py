class Solution:
    def getMaximumGenerated(self, n: int) -> int:
        memo = {0:0, 1:1}

        def dp(n):
            if n in memo:
                return memo[n]
            
            if n % 2 == 0:
                memo[n] = dp(n//2)
            else:
                memo[n] = dp(floor(n/2)) + dp(ceil(n/2))

            return memo[n]

        dp(n)
        
        arr = [0]
        for i in range(n+1):
            arr.append(dp(i))
   
        return max(arr)