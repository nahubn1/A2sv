class Solution:
    def friendRequests(self, n: int, restrictions: List[List[int]], requests: List[List[int]]) -> List[bool]:
        rep = {i: i for i in range(n)}

        def find(x):
            if x == rep[x]:
                return x 
            
            rep[x] = find(rep[x])
            return rep[x]

        def union(u, v):
            rep_u, rep_v = find(u), find(v)

            if rep_u!= rep_v:
                rep[rep_u] = rep_v

        ans = []
        for u, v in requests:
            rep_u, rep_v = find(u), find(v)
            for x, y in restrictions:
                rep_x, rep_y = find(x), find(y)
                if (rep_u == rep_x and rep_v == rep_y) or (rep_u == rep_y and rep_v == rep_x):
                    ans.append(False)
                    break
            else:
                union(u, v)
                ans.append(True)

        return ans