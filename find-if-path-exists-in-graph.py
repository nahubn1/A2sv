class Solution:
    def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        rep = {i: i for i in range(n)}
        def find(x):
            if x == rep[x]:
                return x
            
            rep[x] = find(rep[x])
            return rep[x]
        
        rank = [1]*n 
        def union(u, v):
            rep_u = find(u)
            rep_v = find(v)

            if rank[rep_u] > rank[rep_v]:
                rep[rep_v] = rep_u
                rank[rep_u] += rank[rep_v]
            else:
                rep[rep_u] = rep_v
                rank[rep_v] += rank[rep_u]
        
        for u, v in edges:
            union(u, v)
        
        return find(source) == find(destination)