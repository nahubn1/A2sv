class Solution:
    def eventualSafeNodes(self, graph: List[List[int]]) -> List[int]:
        n = len(graph)
        outBranches = [0]*n
        inBranches = defaultdict(list)

        que = deque()
        for i in range(n):
            if graph[i]:
                for j in graph[i]:
                    inBranches[j].append(i)
                    outBranches[i] += 1
            else:
                que.append(i)
        
        ans = []
        while que:
            state = que.popleft()
            ans.append(state)

            for neigbor in inBranches[state]:
                outBranches[neigbor] -= 1
                if outBranches[neigbor] == 0:
                    que.append(neigbor)
        
        ans.sort()
        return ans