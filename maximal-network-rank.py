class Solution:
    def maximalNetworkRank(self, n: int, roads: List[List[int]]) -> int:
        graph = defaultdict(set)
        for x, y in roads:
            graph[x].add(y)
            graph[y].add(x)
        
        max_rank = 0
        for i in range(n):
            for j in range(i+1, n):
                rank = len(graph[i]) + len(graph[j]) - (i in graph[j])
                max_rank = max(max_rank, rank)

        return max_rank