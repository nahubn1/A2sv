class Solution:
    def isvalid(self, capacity):
        dayload = 0
        total_days = 1
        for weight in self.weights:
            if dayload+weight > capacity:
                total_days += 1
                dayload = weight
            else:
                dayload += weight

        return total_days <= self.days

    def shipWithinDays(self, weights: List[int], days: int) -> int:
        self.weights = weights
        self.days = days

        start, end = max(weights), sum(weights)
        ans = None
        while start <= end:
            middle = (start+end)//2
            valid = self.isvalid(middle)
            
            if not valid:
                start = middle + 1
            else:
                ans = middle
                end =  middle - 1
        
        return ans