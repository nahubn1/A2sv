class Solution:
    def maxKDivisibleComponents(self, n: int, edges: List[List[int]], values: List[int], k: int) -> int:
    
        graph = defaultdict(list)

        for i in range(len(edges)):
            u, v = edges[i]
            
            graph[u].append(v)
            graph[v].append(u)
        
        @cache
        def dp(u, v):
        
            ans = values[v]

            for w in graph[v]:
                if w != u: 
                    ans += dp(v, w)
            
            return ans

        count = 1
        
        for u, v in edges:
            if dp(u, v) % k == dp(v, u) % k ==0:
                count += 1
        
        return count