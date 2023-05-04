class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        for i in range(len(stones)): stones[i] *= -1
        heapify(stones)

        while stones:
            if len(stones) == 1:
                return -1*stones[0]

            y = heappop(stones)
            x = heappop(stones)

            if x != y:
                heappush(stones, y-x)
        
        return 0