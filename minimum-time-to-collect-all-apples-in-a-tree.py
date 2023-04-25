class Solution:
    def minTime(self, n: int, edges: List[List[int]], hasApple: List[bool]) -> int:
        graph = defaultdict(list)
        for a, b in edges:
            graph[a].append(b)
            graph[b].append(a)
        
        def dfs(parent, node):

            path = 0
            for child in graph[node]:
                if child != parent:
                    path += dfs(node, child)
            
            if hasApple[node]:
                hasApple[parent] = True
                print(node)
                return 1 + path
            else:
                return 0
            
        return 2*(dfs(0, 0) - hasApple[0])