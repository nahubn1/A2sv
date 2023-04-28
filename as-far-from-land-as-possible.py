class Solution:
    def maxDistance(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        directions = [(1, 0), (0, 1), (0, -1), (-1, 0)]
        isValid = lambda r, c: 0 <= r < m and 0 <= c < n and grid[r][c] == 0

        que = deque()
        land, water = (False, False)
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    land = True
                    que.append((i, j))
                else:
                    water = True
        
        if land and water:
            dist = 0
            while que:
                lev_len = len(que)
                for _ in range(lev_len):
                    r, c = que.popleft()

                    for r_step, c_step in directions:
                        r_new, c_new = r+r_step, c+c_step

                        if isValid(r_new, c_new):
                            grid[r_new][c_new] = 1
                            que.append((r_new, c_new))
                
                dist += 1
            
            return dist-1

        else:
            return -1