class Solution:
    def mostPoints(self, questions: List[List[int]]) -> int:
        n = len(questions)
        memo = {}
        def dp(i):
            if i in memo:
                return memo[i]

            if i >= n:
                return 0

            memo[i] = max(dp(i+1), dp(i + questions[i][1] + 1) + questions[i][0])
            return memo[i]
        

        return dp(0)