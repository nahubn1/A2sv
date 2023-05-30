class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:


        memo = {0:0}

        def dp(num):
        
            if num < 0:
                return inf

            if num in memo: 
                return memo[num]

            minn = inf
            for c in coins:
                minn = min(minn, dp(num-c))

            memo[num] = minn + 1

            return memo[num]

        ans = dp(amount)
        return ans if ans < inf else -1