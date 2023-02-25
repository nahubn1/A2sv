class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        
        total_dist = max(trips, key = lambda x: x[2])[2]

        capacity_needed = [0]*(total_dist+1)
        
        for pasg, start, end in trips:
            capacity_needed[start] += pasg
            capacity_needed[end] -= pasg
                
        capacity_needed = list(accumulate(capacity_needed))
        
        return max(capacity_needed) <= capacity