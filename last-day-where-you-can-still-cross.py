class Solution:
    def latestDayToCross(self, row: int, col: int, cells: List[List[int]]) -> int:
        n = len(cells)
        rep = {tuple(cell): tuple(cell) for cell in cells}
        directions = [(1, 1), (1, 0), (1, -1), (0, 1), (0, -1), (-1, 1), (-1, 0), (-1, -1)]
        def find(x):
            path = []
            while rep[x] != x:
                path.append(x)
                x = rep[x]
            for y in path:
                rep[y] = x
                
            return x


        rank = defaultdict(lambda:1)
        def union(u, v):
            rep_u = find(u)
            rep_v = find(v)
            if rep_u != rep_v:
                if rank[rep_u] > rank[rep_v]:
                    lakeSpan[rep_u] = lakeSpan[rep_u].union(lakeSpan[rep_v])
                    rep[rep_v] = rep_u
                    rank[rep_u] += rank[rep_v]
                else:
                    lakeSpan[rep_v] = lakeSpan[rep_v].union(lakeSpan[rep_u])
                    rep[rep_u] = rep_v
                    rank[rep_v] += rank[rep_u]
        
        waters = set()
        lakeSpan = {}
        for day, (r, c) in enumerate(cells):
            lakeSpan[(r, c)] = set([c])
            waters.add((r, c))
            repsentative = (r, c)
            for r_step, c_step in directions:
                r_new, c_new = r+r_step, c+c_step
                if (r_new, c_new) in waters:
                    print('>', r_new, c_new)
                    union((r, c), (r_new, c_new))
                    repsentative = find((r, c)) 
                    
            if len(lakeSpan[repsentative]) == col:
                return day