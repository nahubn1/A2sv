class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        graph = defaultdict(list)
        for u, v, p in flights:
            graph[u].append((v, p))

        heap = [(0, src, 0)]
        proccesed = set()

        while heap:
            price, node, stop = heappop(heap)
            
            if node == dst:
                return price

            if stop > k or (node, stop) in proccesed:
                continue
            
            proccesed.add((node, stop))

            for neigbor, p in graph[node]:
                heappush(heap, (price + p, neigbor, stop+1))

        return -1