class Solution:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        m, n = len(mat), len(mat[0])
        ans  = [[-1]*n for _ in range(m)]
        isValid = lambda r, c: 0 <= r < m and 0 <= c < n and mat[r][c] == 1
        directions = [(1, 0), (0, 1), (0, -1), (-1, 0)]

        def bfs():
            que = deque()
            for i in range(m):
                for j in range(n):
                    if mat[i][j] == 0:
                        que.append((i, j))
            
            level = 0
            while que:
                lev_len = len(que)

                for _ in range(lev_len):
                    r, c = que.popleft()
                    ans[r][c] = level

                    for r_step, c_step in directions:
                        if isValid(r+r_step, c+c_step):
                            mat[r+r_step][c+c_step] = 0
                            que.append((r+r_step, c+c_step))

                level += 1
        
        bfs()
        return ans