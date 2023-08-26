class Solution:
    def knightProbability(self, n: int, k: int, row: int, column: int) -> float:

        direc = [(1, 2), (1, -2), (-1, 2), (-1, -2), (2, 1), (2, -1), (-2, 1), (-2, -1)]
        isValid = lambda r, c: 0 <= r < n and 0 <= c < n 

        @cache
        def dp(k, r, c):
        
            if k == 0:
                return 1

            prob = 0
            for r_step, c_step in direc:
                r_new = r + r_step
                c_new = c + c_step

                if isValid(r_new, c_new):
                    prob += (1/8)*dp(k-1, r_new, c_new)
            
            return prob
        
        return dp(k, row, column)