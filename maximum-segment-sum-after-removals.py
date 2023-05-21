class Solution:
    def maximumSegmentSum(self, nums: List[int], removeQueries: List[int]) -> List[int]:
        n = len(nums)
        weight = {i: nums[i] for i in range(n)}
        rep = {i: i for i in range(n)}

        def find(x):
            if x == rep[x]:
                return x
            
            rep[x] = find(rep[x])
            return rep[x]

        rank = [1]*n
        def union(u, v):
            
            rep_u = find(u)
            rep_v = find(v)

            if rep_u != rep_v:  
                if weight[rep_u] > weight[rep_v]: 
                    rep[rep_v] = rep_u
                    weight[rep_u] += weight[rep_v]
                else:
                    rep[rep_u] = rep_v
                    weight[rep_v] += weight[rep_u]

        
        heap = []
        graph = [0]*n
        ans = [0]*n
        for i in range(n-1, -1, -1):
            idx = removeQueries[i]
            graph[idx] = nums[idx]

            if heap: ans[i] = -heap[0]
            
            
            if idx > 0 and graph[idx-1]:
                union(idx-1, idx)
            if idx < n-1 and graph[idx+1]:
                union(idx, idx+1)
            
            heappush(heap, -weight[find(idx)])

        return ans