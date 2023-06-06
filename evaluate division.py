class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        ratios = defaultdict(list)
        for (a, b), v in zip(equations,values):
            ratios[a].append((b, v))
            ratios[b].append((a, 1/v))
        
        def dfs(visited, start, end, r):
            visited.add(start)
            if start == end:
                return r
            
            for neigbor, ratio in ratios[start]:
                if neigbor not in visited:
                    path = dfs(visited, neigbor, end, r*ratio)
                    if path != -1:
                        return path

            return -1
        
        ans = []
        for u, v in queries:
            if u not in ratios or v not in ratios:
                ans.append(-1)
            else:
                ans.append(dfs(set(), u, v, 1))
        
        return ans
