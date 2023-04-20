class Solution:
    def countSubTrees(self, n: int, edges: List[List[int]], labels: str) -> List[int]:
        graph = defaultdict(list)

        for i, j in edges:
            graph[i].append(j)
            graph[j].append(i)
        
        tree = defaultdict(list)
        visited = set()
        def buildTree(node):
            visited.add(node)
            
            for neighbor in graph[node]:
                if neighbor not in visited:
                    tree[node].append(neighbor)
                    buildTree(neighbor)

        buildTree(0)
        ans = [0]*n
        count = defaultdict(int)
        def dfs(node):
            before = count[labels[node]]
            for child in tree[node]:
                dfs(child)
            
            count[labels[node]] += 1
            ans[node] = count[labels[node]] - before

        dfs(0) 
        return ans