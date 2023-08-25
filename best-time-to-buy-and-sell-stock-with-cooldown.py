class Solution:
    def maxProfit(self, prices: List[int]) -> int:

        dp = defaultdict(int)
        for i in range(len(prices)-1, -1, -1):
            for haveStock in [True, False]:
                if haveStock:
                    sell = dp[(i+2, False)] + prices[i]
                    leave = dp[(i+1), True]
                    dp[(i, True)] = max(sell, leave)
                else:
                    buy = dp[(i+1), True] - prices[i]
                    leave = dp[(i+1), False]
                    dp[(i, False)] = max(buy, leave)
                    
        return dp[(0, False)]