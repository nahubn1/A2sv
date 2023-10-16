class Solution:
    def unhappyFriends(self, n: int, preferences: List[List[int]], pairs: List[List[int]]) -> int:
        ranking = {}
        for i in range(n):
            rank = 1
            for u in preferences[i]:
                ranking[(i, u)] = rank
                rank += 1

        unhappy = set()
        visited = set()
        for x, y in pairs:
            for u, v in visited:
                if ranking[(x, u)] < ranking[(x, y)] and  ranking[(u, x)] < ranking[(u, v)]:
                    unhappy.add(x)
                    unhappy.add(u)
                if ranking[(y, u)] < ranking[(y, x)] and  ranking[(u, y)] < ranking[(u, v)]:
                    unhappy.add(y)
                    unhappy.add(u)
                
            visited.add((x, y))
            visited.add((y, x))
        
        return len(unhappy)