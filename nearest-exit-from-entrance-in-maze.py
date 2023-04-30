class Solution:
    def nearestExit(self, maze: List[List[str]], entrance: List[int]) -> int:
        
        m, n = len(maze), len(maze[0])
        directions = [(1, 0), (0, -1), (0, 1), (-1, 0)]
        isValid = lambda r, c: 0 <= r < m and 0 <= c < n and maze[r][c] == '.'
        isBoarder = lambda r, c: r == 0 or r == m-1 or c == 0 or c == n-1

        que = deque([entrance])
        step = 0
        while que:
            lev_len = len(que)
            for _ in range(lev_len):
                r, c = que.popleft()
    
                if isBoarder(r, c)  and [r, c] != entrance:
                    return step

                for r_step, c_step in directions:
                    if isValid(r+r_step, c+c_step):
                        maze[r+r_step][c+c_step] = '+'
                        que.append((r+r_step, c+c_step))
                
            step += 1
        
        return -1