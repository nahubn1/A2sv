class Solution:
    def removeStones(self, stones: List[List[int]]) -> int:
        stones = list(map(tuple, stones))
        rep = {tuple(stone): tuple(stone) for stone in stones}
        def find(cell):
            if rep[cell] == cell:
                return cell
            
            rep[cell] = find(rep[cell])
            return rep[cell]
        
        rank = defaultdict(lambda:1) 

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
        
        for i in range(len(stones)):
            for j in range(i+1, len(stones)):
                u, v = tuple(stones[i]), tuple(stones[j])
                if u[0] == v[0] or u[1] == v[1]:
                    union(u, v)
        ans = 0
        considered = set()
        for stone in stones:
            rStone = find(stone)
            if rStone not in considered:
                ans += (rank[rStone] - 1)
                considered.add(rStone)
        
        return ans