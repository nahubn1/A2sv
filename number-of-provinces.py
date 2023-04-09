class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        graph = defaultdict(list)
        for i in range(len(isConnected)):
            for j in range(i+1, len(isConnected)):
                if isConnected[i][j] == 1:
                    graph[i].append(j)
                    graph[j].append(i)

        visited = set()
        def dfs(vertex):           
            visited.add(vertex)

            for i in graph[vertex]:
                if i not in visited: 
                    dfs(i)
            
        provinces = 0
        for i in range(len(isConnected)):
            if i not in visited:
                provinces += 1
                dfs(i)
        
        return provinces