class Solution:
    def possibleBipartition(self, n: int, dislikes: List[List[int]]) -> bool:
        haters = defaultdict(set)
        for a, b in dislikes:
            haters[a].add(b)
            haters[b].add(a)
        
        color = [0]*(n+1)

        def dfs(person, c):
            
            color[person] = c
            for enemy in haters[person]:
                if color[enemy] == c:
                    return False
                elif not color[enemy] and not dfs(enemy, -c):
                    return False
                
            return True
        
        for p in range(1, n+1):
            if not color[p]:
                if not dfs(p, 1):
                    return False

        return True