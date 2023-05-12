class Solution:
    def loudAndRich(self, richer: List[List[int]], quiet: List[int]) -> List[int]:
        n = len(quiet)
        graph = defaultdict(list)
        for a, b in richer:
            graph[b].append(a)
        
        color = [0]*n
        def dfs(node):
            if ans[node] != -1:
                return ans[node]

            humble = (quiet[node], node)
            for better in graph[node]:
                humble = min(humble, dfs(better))
            
            ans[node] = humble
            return humble
        
        ans = [-1]*n
        for i in range(n):
            dfs(i)

        return [person for quitness, person in ans]