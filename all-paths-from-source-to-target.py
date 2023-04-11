class Solution:
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        ans = []
        def dfs(vertex, arr):
            if vertex == len(graph)-1:
                ans.append(arr)
                return
            
            for child in graph[vertex]:
                dfs(child, arr+[child])
        
        dfs(0, [0])
        return ans