class Solution:
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
        accounts = [[acc[0], set(acc[1:])] for acc in accounts]
        n = len(accounts)
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
        
        for i in range(n):
            for j in range(i+1, n):
                if i != j:
                    emails_i, emails_j = accounts[i][1], accounts[j][1]
                    if emails_i.intersection(emails_j):
                        union(i, j)
        

        merged = defaultdict(set)
        for i in range(n):
            representative, emails = find(i), accounts[i][1]
            merged[representative] = merged[representative].union(emails)

        ans = []
        for i in merged:

            ans.append([accounts[i][0], *sorted(merged[i])])
        
        return ans