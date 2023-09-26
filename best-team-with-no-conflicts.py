class Solution:
    def bestTeamScore(self, scores: List[int], ages: List[int]) -> int:
        players = list(zip(ages, scores))
        players.sort()

        dp = [0]*len(players) 
        for i in range(len(players)):
            dp[i] += players[i][1]
            for j in range(i):
                if players[i][0] == players[j][0] or players[i][1] >= players[j][1]:
                    dp[i] = max(dp[i], dp[j]+players[i][1])
        
        return max(dp)