class Solution:
    def mincostTickets(self, days: List[int], costs: List[int]) -> int:
        
        @cache
        def dp(i):
            if i >= len(days):
                return 0
            
            i_1 = bisect_left(days, days[i]+1)
            i_7 = bisect_left(days, days[i]+7)
            i_30 = bisect_left(days, days[i]+30)

            return min(costs[0]+dp(i_1), costs[1]+dp(i_7), costs[2]+dp(i_30))
        
        return dp(0)