class Solution:
    def isPrintable(self, targetGrid: List[List[int]]) -> bool:
        n, m = len(targetGrid), len(targetGrid[0])
        rectangle = defaultdict(lambda: [n, m, 0, 0]) #[rs, cs, re, ce] 

        for i in range(n):
            for j in range(m):
                color = targetGrid[i][j]
                rectangle[color][0] = min(rectangle[color][0], i)
                rectangle[color][1] = min(rectangle[color][1], j)
                rectangle[color][2] = max(rectangle[color][2], i)
                rectangle[color][3] = max(rectangle[color][3], j)
        
        graph = defaultdict(list)
        for col in rectangle:
            rs, cs, re, ce = rectangle[col]
            for i in range(rs, re+1):
                for j in range(cs, ce+1):
                    if targetGrid[i][j] != col:
                        graph[col].append(targetGrid[i][j])
        
        status = defaultdict(int)
        def dfs(node): 
            if status[node] == 2:
                return True

            status[node] = 1
            for ngb in graph[node]:
                if status[ngb] == 1 or not dfs(ngb):
                    return False
            
            status[node] = 2
            return True
        
        for col in rectangle:
            if status[col] == 0 and not dfs(col):
                return False
        
        return True

        