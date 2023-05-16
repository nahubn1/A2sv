class Solution:
    def buildMatrix(self, k: int, rowConditions: List[List[int]], colConditions: List[List[int]]) -> List[List[int]]:

        rowPreReq = defaultdict(list)
        for a, b in rowConditions:
            rowPreReq[b-1].append(a-1)
        
        colPreReq = defaultdict(list)
        for l, r in colConditions:
            colPreReq[r-1].append(l-1)

        def dfs(node, color, graph, arr):
            if color[node] == 2:
                return True
            elif color[node] == 0:
                color[node] = 1
                if all([dfs(neighbor, color, graph, arr) for neighbor in graph[node]]):
                    color[node] = 2
                    arr.append(node)
                    return True

        
        rowOrder = []
        colOrder = []
        rowColor = [0]*k
        colColor = [0]*k
        for i in range(k):
            if not dfs(i, rowColor, rowPreReq, rowOrder): 
                return []
            if not dfs(i, colColor, colPreReq, colOrder):
                return []
        
        matrix = [[0]*k for _ in range(k)]
        for i in range(k):
            for j in range(k):
                if colOrder[j] == rowOrder[i]:
                    matrix[i][j] = rowOrder[i]+1
        
        return matrix