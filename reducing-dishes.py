class Solution:
    def maxSatisfaction(self, satisfaction: List[int]) -> int:
        n = len(satisfaction)
        satisfaction.sort()

        r_sum = 0
        LTcoeff = 0
        for i in range(n-1, -1, -1):
            r_sum += satisfaction[i]

            if r_sum < 0:
                return LTcoeff
            else:
                LTcoeff += r_sum    
            
        return LTcoeff