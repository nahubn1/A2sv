class Solution:
    def longestPath(self, parent: List[int], s: str) -> int:
        tree = defaultdict(list)
        character = {}
        self.lonPath = 1

        for i, p in enumerate(parent):
            character[i] = s[i]
            if p != -1:
                tree[p].append(i)
        
        def dfs(vertex):
            if not tree[vertex]:
                return 1
            
            candidates = [0, 0]
            for child in tree[vertex]:
                path = dfs(child)
                if character[child] != character[vertex]:
                    candidates.append(path)
            
            candidates.sort()
            self.lonPath = max(self.lonPath, sum(candidates[-2:]) + 1) 

            return max(candidates) + 1

        dfs(0)

        return self.lonPath