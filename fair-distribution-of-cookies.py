class Solution:
    def distribute(self, idx, buckets):
        if idx == self.n:
            self.minDistribution = max(buckets)
            return self.minDistribution

        candidates = []
        for i in range(len(buckets)):
            buckets[i] += self.cookies[idx]
            if max(buckets) < self.minDistribution:
                candidates.append(self.distribute(idx+1, buckets))
            buckets[i] -= self.cookies[idx]
        
        return min(candidates) if candidates else self.minDistribution
            
    def distributeCookies(self, cookies: List[int], k: int) -> int:
        buckets = [0]*k
        self.minDistribution = float('inf')
        self.n = len(cookies)
        self.cookies = cookies
        return self.distribute(0, buckets)