class Solution:
    def largestIsland(self, grid: List[List[int]]) -> int:
        n = len(grid)

        rep = {(i, j): (i, j) for i in range(n) for j in range(n)}

        def find(x):
            if x == rep[x]:
                return x
            
            rep[x] = find(rep[x])
            return rep[x]
        
        rank = defaultdict(lambda:1)
        def union(u, v):
            repU = find(u)
            repV = find(v)

            if repU != repV:
                if rank[u] > rank[v]:
                    rep[repV] = repU
                    rank[repU] += rank[repV]
                else:
                    rep[repU] = repV
                    rank[repV] += rank[repU]
        
        direc = [(1, 0), (0, 1), (-1, 0), (0, -1)]
        inBound = lambda i, j: 0 <= i < n and 0 <= j < n

        for i in range(n):
            for j in range(n):
                if grid[i][j] == 1:
                    for iStep, jStep in direc:
                        iNew, jNew = i+iStep, j+jStep
                        if inBound(iNew, jNew) and grid[iNew][jNew] == 1:
                            union((i, j), (iNew, jNew))
        
        ans =  max(rank.values()) if rank else 1

        for i in range(n):
            for j in range(n):
                if grid[i][j] == 0:
                    island = 1
                    visited = set()
                    for iStep, jStep in direc:
                        iNew, jNew = i+iStep, j+jStep
                        if inBound(iNew, jNew) and grid[iNew][jNew] == 1:
                            repIJ = find((iNew, jNew))
                            if repIJ not in visited:
                                island += rank[repIJ]
                                visited.add(repIJ)
                    
                    ans = max(ans, island)
        
        return ans