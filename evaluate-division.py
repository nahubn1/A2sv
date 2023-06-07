class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        ratio = defaultdict(lambda: 1)
        rep = {}
        for a, b in equations: 
            rep[a] = a
            rep[b] = b
     
        def find(x):
            if rep[x] == x:
                return x
            
            temp = rep[x]
            rep[x] = find(rep[x])
            ratio[x] *= ratio[temp]
            return rep[x]

        def union(a, b, val):
            rep_a, rep_b = find(a), find(b)

            if rep_a!= rep_b:
                rep[rep_a] = rep_b
                ratio[rep_a] = val / (ratio[a] / ratio[b])

        for (a, b), val in zip(equations, values):
            union(a, b, val)

        ans = []
        for u, v in queries:
            
            if u not in rep or v not in rep or find(u) != find(v):
                ans.append(-1)
            else:
                ans.append(ratio[u] / ratio[v])    

        return ans