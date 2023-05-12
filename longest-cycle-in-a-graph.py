class Solution:
    def longestCycle(self, edges: List[int]) -> int:
        n = len(edges)
        graph = defaultdict(list)
        for i, val in enumerate(edges):
            if val != -1:
                graph[i].append(val)

        color = [0]*n
        def dfs(node, level):
            if color[node] == 2:
                return True

            elif color[node] == 0:
                color[node] = (1, level)
                if all([dfs(neighbor, level + 1) for neighbor in graph[node]]):
                    color[node] = 2
                    return True
                else:
                    color[node] = 2
                    return False
            else:
                self.cycle = max(self.cycle, level - color[node][1])
                return False
        
        self.cycle = -1
        for i in range(n):
            if color[i] == 0:
                dfs(i, 0)
        
        return self.cycle