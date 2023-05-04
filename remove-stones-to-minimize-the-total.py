class Solution:
    def minStoneSum(self, piles: List[int], k: int) -> int:

        for i in range(len(piles)): 
            piles[i] *= -1
        heapify(piles)

        for _ in range(k):
            largest = -heappop(piles)
            heappush(piles, -(largest - floor(largest/2)))
        
        return -sum(piles)