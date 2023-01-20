class Solution:
    def maxCoins(self, piles: List[int]) -> int:
        piles.sort()
        n = len(piles)
        return sum(piles[n-2:n - (2*n//3)-1:-2])