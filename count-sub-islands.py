class Solution:
    def countSubIslands(self, grid1: List[List[int]], grid2: List[List[int]]) -> int:
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        def dfs(r, c):
            if grid1[r][c] == 0:
                self.isSub = False
            
            grid2[r][c] = 0
            for r_step, c_step in directions:
                if 0 <= r+r_step < len(grid1) and 0 <= c+c_step < len(grid1[0]):
                    if grid2[r+r_step ][c+c_step]:
                        dfs(r+r_step, c+c_step)
        

        count = 0
        for i in range(len(grid1)):
            for j in range(len(grid1[0])):
                self.isSub = True
                if grid2[i][j] == 1:
                    dfs(i, j)
                    if self.isSub:
                        count += 1

        return count