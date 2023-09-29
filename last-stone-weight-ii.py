class Solution:
    def lastStoneWeightII(self, stones: List[int]) -> int:

        total = sum(stones)
        ans = inf
        @cache
        def dp(i, curr):
            nonlocal ans, total
            ans = min(ans, abs(total-2*curr))
            if i < len(stones):
                dp(i+1, curr+stones[i])
                dp(i+1, curr)
        
        dp(0, 0)
        return ceil(ans)