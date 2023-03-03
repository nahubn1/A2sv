from math import ceil
class Solution:
    def isvalid(self, k):
        total = 0
        for pile in self.piles:
            total += ceil(pile/k)
        
        return total <= self.h

    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        self.piles = piles
        self.h = h

        start, end = 1, max(piles)

        while start <= end:
            middle = (start+end)//2
            if not self.isvalid(middle):
                start = middle +1 
            elif middle != 1 and self.isvalid(middle) and self.isvalid(middle-1):
                end = middle - 1
            else:
                return middle