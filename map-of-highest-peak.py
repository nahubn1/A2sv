class Solution:
    def highestPeak(self, isWater: List[List[int]]) -> List[List[int]]:
        m, n = len(isWater), len(isWater[0])
        directions = [(1, 0), (0, 1), (0, -1), (-1, 0)]
        isValid = lambda r, c: 0 <= r < m and 0 <= c < n

        que = deque()
        visited = set()
        for i in range(m):
            for j in range(n):
                if isWater[i][j] == 1:
                    que.append((i, j))
                    visited.add((i, j))
        
        height = 0
        while que:
            
            lev_len = len(que)
            for _ in range(lev_len):
                r, c = que.popleft()
                isWater[r][c] = height

                for r_step, c_step in directions:
                    r_new, c_new = r+r_step, c+c_step
                    if isValid(r_new, c_new) and (r_new, c_new) not in visited:
                        que.append((r_new, c_new))
                        visited.add((r_new, c_new))
            
            height += 1
        
        return isWater