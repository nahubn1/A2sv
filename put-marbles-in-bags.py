class Solution:
    def putMarbles(self, weights: List[int], k: int) -> int:
        if len(weights) <= 2:
            return 0

        middles = []
        for i in range(len(weights)-1):
            middles.append(weights[i]+weights[i+1])
        middles.sort()
        
        return sum(middles[len(weights)-k:]) - sum(middles[:k-1])