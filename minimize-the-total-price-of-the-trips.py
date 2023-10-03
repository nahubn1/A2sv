class Solution:
    def minimumTotalPrice(self, n: int, edges: List[List[int]], price: List[int], trips: List[List[int]]) -> int:
        graph = defaultdict(list)
        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)
        
        net_price = [0]*n

        def dfs(parent, node, sink):
            if node == sink:
                net_price[node] += price[node]
                return True
            
            for neighbor in graph[node]:
                if parent != neighbor and dfs(node, neighbor, sink):
                    net_price[node] += price[node]
                    return True
            
            return False
        
        for source, sink in trips:
            dfs(-1, source, sink)

        @cache
        def dp(parent, node, half):

            use = net_price[node]//2 if half else inf
            leave = net_price[node]
            for neigbor in graph[node]:
                if neigbor != parent:
                    use += dp(node, neigbor, False)
                    leave += dp(node, neigbor, True)
            
            return min(use, leave)

        return dp(-1, 0, True)