class Solution:
    def restoreArray(self, adjacentPairs: List[List[int]]) -> List[int]:
        graph = defaultdict(list)
        
        for a, b in adjacentPairs:
            graph[a].append(b)
            graph[b].append(a)
        
        for node in graph:
            if len(graph[node]) == 1:
                startingNode = node
                break

        ans = []
        def dfs(parent, node):
            ans.append(node)

            for adj in graph[node]:
                if adj != parent:
                    dfs(node, adj)
        
        dfs(None, startingNode)
        return ans