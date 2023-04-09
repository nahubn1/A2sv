class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:

        def discover(r, c):
            grid[r][c] = 0

            Area = 1
            for r_step, c_step in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
                if 0 <= r+r_step < len(grid) and 0 <= c+c_step < len(grid[0]):
                    if grid[r+r_step][c+c_step] == 1:
                        Area += discover(r+r_step, c+c_step)
            
            return Area
        

        maxArea = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1:
                    maxArea = max(maxArea, discover(i, j))
        
        return maxArea