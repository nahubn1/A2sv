class Solution:
    def sortItems(self, n: int, m: int, group: List[int], beforeItems: List[List[int]]) -> List[int]:
        groupItems = [[] for _ in range(m)]
        for i in range(n):
            if group[i] == -1:
                group[i] = m
                groupItems.append([i])
                m += 1
            else:
                groupItems[group[i]].append(i)

        interGroup = defaultdict(list)
        intraGroup = defaultdict(list)
        for i, arr in enumerate(beforeItems):
            for j in arr:
                if group[i] == group[j]:
                    intraGroup[i].append(j)
                else:
                    interGroup[group[i]].append(group[j])
        
        def dfs(node, graph, color):
            if color[node] == 2:
                return True
            elif color[node] == 0:
                color[node] = 1

                if all([dfs(neighbor, graph, color) for neighbor in graph[node]]):
                    ans.append(node)
                    color[node] = 2
                    return True
        
        color = [0]*n
        for i in range(m):
            ans = []
            for j in groupItems[i]:
                if not dfs(j, intraGroup, color):
                    print('>')
                    return []
            
            groupItems[i] =  ans
        
        color = [0]*m
        ans = []
        for i in range(m):
            if not dfs(i, interGroup, color):
                return []

        sortedGroup = ans

        res = []
        for i in sortedGroup:
            res.extend(groupItems[i])
        
        return res