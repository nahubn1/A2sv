class Solution:
    def gridGame(self, grid: List[List[int]]) -> int:
        n = len(grid[0])
        preSum1 = [0]
        preSum2 = [0]

        for i in range(n):
            preSum1.append(preSum1[-1]+grid[0][n-i-1])
            preSum2.append(preSum2[-1]+grid[1][i])
        preSum1.reverse()

        ans = inf
        for i in range(n):
            ans = min(ans, max(preSum1[i+1], preSum2[i]))
        
        return ans