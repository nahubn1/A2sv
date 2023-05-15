class Solution:
    def checkIfPrerequisite(self, numCourses: int, prerequisites: List[List[int]], queries: List[List[int]]) -> List[bool]:
        inDegree = [0]*numCourses
        graph = defaultdict(list)

        for a, b in prerequisites:
            graph[a].append(b)
            inDegree[b] += 1

        que = deque() 
        for i in range(numCourses):
            if inDegree[i] == 0:
                que.append(i)
        
        ans = [set() for _ in range(numCourses)]
        while que:
            node = que.popleft()
            
            for child in graph[node]:
                ans[child].add(node)
                ans[child] = ans[child].union(ans[node])

                inDegree[child] -= 1
                if inDegree[child] == 0:
                    que.append(child)

        answer = []
        for u, v in queries:
            answer.append(u in ans[v])
            
        return answer