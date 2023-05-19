class Solution:
    def equationsPossible(self, equations: List[str]) -> bool:
        rep = {chr(i): chr(i) for i in range(97, 123)}

        def find(x):
            if x == rep[x]:
                return x
            
            rep[x] = find(rep[x])
            return rep[x]
        
        rank = defaultdict(lambda: 1)
        def union(u, v):
            rep_u = find(u)
            rep_v = find(v)

            if rank[rep_u] > rank[rep_v]:
                rep[rep_v] = rep_u
                rank[rep_u] += rank[rep_v]
            else:
                rep[rep_u] = rep_v
                rank[rep_v] += rank[rep_u]
        
        notEqls = []
        for eqn in equations:
            x1, op, x2 = eqn[0], eqn[1], eqn[3]
            if op == '=':
                union(x1, x2)
            else:
                notEqls.append((x1, x2))
        
        return all([find(x1) != find(x2) for x1, x2 in notEqls])