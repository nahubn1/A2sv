class Solution:
    def minimumHammingDistance(self, source: List[int], target: List[int], allowedSwaps: List[List[int]]) -> int:
        n = len(source)
        rep = {i: i for i in range(n)}
        rank = {i: 1 for i in range(n)}
        group = {i: Counter([source[i]]) for i in range(n)}

        def find(x):
            if x == rep[x]:
                return x
            
            rep[x] = find(rep[x])
            return rep[x]

        def union(u, v):
            
            rep_u = find(u)
            rep_v = find(v)

            if rep_u != rep_v:  
                if rank[rep_u] > rank[rep_v]:
                    rep[rep_v] = rep_u
                    rank[rep_u] += rank[rep_v]
                    group[rep_u] += group[rep_v]
                else:
                    rep[rep_u] = rep_v
                    rank[rep_v] += rank[rep_u]
                    group[rep_v] += group[rep_u]
            
        for a, b in allowedSwaps:
            union(a, b)
        
        ham_dist = 0
        for i in range(n):
            if  group[find(i)][target[i]]:
                group[find(i)][target[i]] -= 1     
            else:
                ham_dist += 1
        
        return ham_dist