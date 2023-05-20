class Solution:
    def smallestStringWithSwaps(self, s: str, pairs: List[List[int]]) -> str:
        rep = {i: i for i in range(len(s))}
        def find(x):
            path = []
            while rep[x] != x:
                path.append(x)
                x = rep[x]
            for y in path:
                rep[y] = x
                
            return x


        rank = [1]*len(s)
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
        
        for u, v in pairs:
            if find(u) != find(v):
                union(u, v)
        
        groupsByIndx = defaultdict(list)
        groupsByChar = defaultdict(list)

        ans = [0]*len(s)
        for i in range(len(s)):
            groupsByIndx[find(i)].append(i)
            groupsByChar[find(i)].append(s[i])

        for group in groupsByIndx:
            idxes = sorted(groupsByIndx[group])
            chars = sorted(groupsByChar[group])
        
            for i, ch in zip(idxes, chars):
                ans[i] = ch
        
        return ''.join(ans)