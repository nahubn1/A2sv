class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        grid = [[1]*n for i in range(m)]
        print(grid)
        for i in range(1, m):
            for j in range(1, n):
                grid[i][j] = grid[i-1][j] + grid[i][j-1]
        
        return grid[-1][-1]