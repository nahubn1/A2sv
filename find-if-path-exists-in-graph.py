class Solution:
    def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        graph = defaultdict(list)
        for i, j in edges:
            graph[i].append(j)
            graph[j].append(i)
        
        def dfs():
            visited = set()
            stack = [source]
            while stack:        
                if stack[-1] == destination:
                    return True

                for nieghbor in graph[stack.pop()]:
                    if nieghbor not in visited:
                        visited.add(nieghbor)
                        stack.append(nieghbor)
                    
        return dfs()