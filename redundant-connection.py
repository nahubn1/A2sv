class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        graph = defaultdict(list)
        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)
        
        
        def make_cycle(parent, node):
            if node in path:
                return True
            
            path.add(node)

            for child in graph[node]:
                if child != parent and make_cycle(node, child):
                    return True

        for u, v in reversed(edges):
            path =  set()
            if make_cycle(u ,v) and u in path:
                return [u, v]