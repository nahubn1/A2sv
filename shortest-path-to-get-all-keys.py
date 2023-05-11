class Solution:
    def gridConditions(self, grid):
        keys = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == '@':
                    startingPoint =  (i, j)
                elif grid[i][j].islower():
                    keys += 1
        
        return startingPoint, keys
    

    def shortestPathAllKeys(self, grid: List[str]) -> int:
        m, n = len(grid), len(grid[0])

        (r_start, s_start), totalKeys = self.gridConditions(grid)
        keyIndex = {'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5, 'f': 6}

        isValid = lambda r, c: 0 <= r < m and 0 <= c < n
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
    
        que = deque([(r_start, s_start, 0)])
        visited = set([(r_start, s_start, 0)])
        
      
        step = 0
        while que:
            
            for _ in range(len(que)):
                
                r, c, state = que.popleft()
                if state.bit_count() == totalKeys:
                    return step

                for r_step, c_step in directions:
                    r_new, c_new = r+r_step, c+c_step
                    if isValid(r_new, c_new):
                        if grid[r_new][c_new] == '#':
                            continue

                        if grid[r_new][c_new].isupper():
                            keyNeeded = grid[r_new][c_new].lower()
                            if not state & (1 << keyIndex[keyNeeded]):
                                continue

                        if grid[r_new][c_new].islower():
                            state_new = state | (1 << keyIndex[grid[r_new][c_new]])
                        else:
                            state_new = state
                        
                        if (r_new, c_new, state_new) not in visited:
                            que.append((r_new, c_new, state_new))
                            visited.add((r_new, c_new, state_new))
                
            step += 1

        
        return -1