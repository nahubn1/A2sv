class Solution:
    def smallestEquivalentString(self, s1: str, s2: str, baseStr: str) -> str:
        
        rep = {chr(i): chr(i) for i in range(97, 123)}
        def find(x):
            if x == rep[x]:
                return x
            
            rep[x] = find(rep[x])
            return rep[x]
        
        def union(u, v):
            repU = find(u)
            repV = find(v)

            if repU != repV:
                if repU < repV:
                    rep[repV] = repU
                else:
                    rep[repU] = repV
        
        for char1, char2 in zip(s1, s2):
            union(char1, char2)

        ans = []
        for char in baseStr:
            ans.append(find(char))

        return ''.join(ans)