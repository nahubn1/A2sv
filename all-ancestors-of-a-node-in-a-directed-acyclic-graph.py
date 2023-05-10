class Solution:
    def getAncestors(self, n: int, edges: List[List[int]]) -> List[List[int]]:

        inDegree = [0]*n
        graph = defaultdict(list)

        for a, b in edges:
            graph[a].append(b)
            inDegree[b] += 1

        que = deque() 
        for i in range(n):
            if inDegree[i] == 0:
                que.append(i)
        
        ans = [set() for _ in range(n)]
        while que:
            node = que.popleft()
            
            for child in graph[node]:
                ans[child].add(node)
                ans[child] = ans[child].union(ans[node])

                inDegree[child] -= 1
                if inDegree[child] == 0:
                    que.append(child)
        
        return [sorted(ansestors) for ansestors in ans]