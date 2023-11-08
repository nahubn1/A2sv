class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:

        graph = defaultdict(list)
        for (u, v), val in zip(equations, values):
            graph[u].append((v, val))
            graph[v].append((u, 1/val))
        

        def bfs(numerator, denominator):
            if numerator not in graph or numerator not in graph: return -1
            que = deque([(numerator, 1)])
            visited = set([numerator])

            while que:
                node, val = que.pop()
                if node == denominator:
                    return val
                
                for neigbor, newVal in graph[node]:
                    if neigbor not in visited:
                        que.append((neigbor, val*newVal))
                        visited.add(neigbor)
                
            return -1
        
        ans = []
        for n, d in queries:
            ans.append(bfs(n, d))
        
        return ans
            


        