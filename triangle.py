class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        row = len(triangle)
        memo = {}
        def dp(i, j):
            if (i, j) in memo:
                return memo[(i, j)]

            if not(i < row):
                return 0
            
            if not (j < len(triangle[i])):
                return 0

            memo[(i, j)] = min(dp(i+1, j), dp(i+1, j+1)) + triangle[i][j]
            return memo[(i, j)]
        
        return dp(0, 0)