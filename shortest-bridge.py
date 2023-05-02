class Solution:
    def shortestBridge(self, grid: List[List[int]]) -> int:
        n = len(grid)
        directions = [(1, 0), (0, 1), (0, -1), (-1, 0)]
        isValid = lambda r, c: 0 <= r < n and 0 <= c < n 

        island_1 = set()
        def connect(r, c):
            island_1.add((r, c))
        
            for r_step, c_step in directions:
                if isValid(r+r_step, c+c_step) and grid[r][c] == 1 and (r+r_step, c+c_step) not in island_1:
                    connect(r+r_step, c+c_step)
            
    
        
        flag = False
        que = deque()
        visited = set()
        for i in range(n):
            for j in range(n):
                if not flag and grid[i][j] == 1:
                    connect(i, j)
                    flag = True
                
                if flag and grid[i][j] == 1 and (i, j) not in island_1:
                    que.append((i, j))
                    visited.add((i, j))
        
        dist = 0
        while que:
            for _ in range(len(que)):
                r, c = que.popleft()
                if (r, c) in island_1:
                    return dist

                for r_step, c_step in directions:
    
                     if isValid(r+r_step, c+c_step) and (r+r_step, c+c_step) not in visited:
                         que.append((r+r_step, c+c_step))
                         visited.add((r+r_step, c+c_step))
                
            dist += 1

        return -1