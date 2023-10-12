class Solution:
    def numTeams(self, rating: List[int]) -> int:
        
        n = len(rating)
        ans = 0

        for i in range(n):
            left_less = 0
            left_greater = 0
            right_less = 0
            right_greater = 0

            for j in range(n):
                if j < i:
                    if rating[j] < rating[i]:
                        left_less += 1
                    elif rating[j] > rating[i]:
                        left_greater += 1
                elif j > i:
                    if rating[j] < rating[i]:
                        right_less += 1
                    elif rating[j] > rating[i]:
                        right_greater += 1
        
            ans += (left_less * right_greater) + (left_greater * right_less)
        
        return ans