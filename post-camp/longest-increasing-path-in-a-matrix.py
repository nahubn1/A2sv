class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        m, n = len(matrix), len(matrix[0])
        graph = defaultdict(list)
        indegree = [[0]*n for _ in range(m)]
        inBound = lambda i, j: 0 <= i < m and 0 <= j < n
        for i in range(m):
            for j in range(n):
                
                for vi, vj in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
                    i_new, j_new = i+vi, j+vj
                    if inBound(i_new, j_new) and matrix[i][j] < matrix[i_new][j_new]:
                        graph[(i, j)].append((i_new, j_new))
                        indegree[i_new][j_new] += 1
        
        que = deque()
        path = [[0]*n for _ in range(m)]
        for i in range(m):
            for j in range(n):
                if indegree[i][j] == 0:
                    que.append((i, j))
        

        while que:
            i, j = que.popleft()
            path[i][j] += 1
            for i_n, j_n in graph[(i, j)]:
                indegree[i_n][j_n] -= 1
                path[i_n][j_n] = max(path[i_n][j_n], path[i][j])

                if indegree[i_n][j_n] == 0:
                    que.append((i_n, j_n))
            
        return max([max(row) for row in path]) 


