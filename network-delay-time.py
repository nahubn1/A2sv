class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        graph = defaultdict(list)
        for u, v, t in times:
            graph[u-1].append((v-1, t))

        heap = [(k-1, 0)]
        min_time = [inf]*n

        while heap:
            node, t = heappop(heap) 

            if min_time[node] < t:
                continue

            min_time[node] = t

            for neigbor, w in graph[node]:
                if min_time[neigbor] > t+w:
                    heappush(heap, (neigbor, t+w))

        ans = max(min_time)
        return ans if ans < inf else -1