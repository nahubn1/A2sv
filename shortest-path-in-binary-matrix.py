class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        directions = [(1, 1), (1, 0), (1, -1), (0, 1), (0, -1), (-1, 1), (-1, 0), (-1, -1)]
        m, n = len(grid), len(grid[0])
        isClear = lambda r, c: 0 <= r < m and 0 <= c < n and grid[r][c] == 0

        def bfs():
            que = deque()
            if isClear(0, 0): que.append((0, 0))
            
            path = 1
            while que:
                
                lev_len = len(que)
                for _ in range(lev_len):
                    r, c = que.popleft()

                    if (r, c) == (m-1, n-1):
                        return path

                    for r_step, c_step in directions:
                        if isClear(r+r_step, c+c_step):
                            que.append((r+r_step, c+c_step))
                            grid[r+r_step][c+c_step] = 1
                
                path += 1
            
            return -1
        
        return bfs()