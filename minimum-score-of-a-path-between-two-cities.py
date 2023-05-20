class Solution:
    def minScore(self, n: int, roads: List[List[int]]) -> int:
        rep = {i: i for i in range(1, n+1)}
        def find(x):
            path = []
            while rep[x] != x:
                path.append(x)
                x = rep[x]
            for y in path:
                rep[y] = x
                
            return x


        rank = [1]*(n+1)
        def union(u, v):
            rep_u = find(u)
            rep_v = find(v)
            if rep_u != rep_v:
                if rank[rep_u] > rank[rep_v]:
                    rep[rep_v] = rep_u
                    rank[rep_u] += rank[rep_v]
                else:
                    rep[rep_u] = rep_v
                    rank[rep_v] += rank[rep_u]
        
        minEdge = defaultdict(lambda: inf)
        for a, b, wg in roads:
            union(a, b)
            minEdge[a] = min(minEdge[a], wg)
            minEdge[b] = min(minEdge[b], wg)
        
        score = inf
        for i in range(1, n+1):
            if find(i) == find(1):
                score = min(score, minEdge[i])
        
        return score