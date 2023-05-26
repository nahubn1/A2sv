class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        n = len(cost)
        memo = {0: cost[0], 1:cost[1]}

        def dp(n):
            
            if n in memo:
                return memo[n]
            
            memo[n] = min(dp(n-1), dp(n-2)) + cost[n]
            return memo[n]

        return min(dp(n-1), dp(n-2))