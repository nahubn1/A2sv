class Solution:
    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:

        
        graph = defaultdict(list)
        edgeCount = [0]*n
        for a, b in edges:
            graph[a].append(b)
            graph[b].append(a)

            edgeCount[a] += 1
            edgeCount[b] += 1

        que = deque()
        visited = set()
        for i in range(n):
            if edgeCount[i] <= 1:
                que.append(i)
                visited.add(i)

        while n > 2:

            for _ in range(len(que)):
                node = que.popleft()
                edgeCount[node] -= 1
                n -= 1
                for neighbor in graph[node]:
                    if neighbor not in visited:

                        edgeCount[neighbor] -= 1
                        if edgeCount[neighbor] <= 1:
                            que.append(neighbor)
                            visited.add(neighbor)
        
        return que