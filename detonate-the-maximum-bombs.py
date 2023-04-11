class Solution:
    def maximumDetonation(self, bombs: List[List[int]]) -> int:

        graph = defaultdict(list)
        for i in range(len(bombs)):
            xi, yi, ri = bombs[i]
            for j in range(len(bombs)):
                xj, yj, rj = bombs[j]
                if i != j and (xi-xj)**2 + (yi-yj)**2 <= ri**2:
                    graph[i].append(j)
                    
                    
        visited = set()
        def dfs(vertex):
            
            visited.add(vertex)
            
            connected = 1
            for child in graph[vertex]:
                if child not in visited:
                    connected += dfs(child)
            
            return connected
        
        maxDen = 0
        for vertex in range(len(bombs)):
            visited.clear()
            maxDen = max(maxDen, dfs(vertex))
        
        return maxDen