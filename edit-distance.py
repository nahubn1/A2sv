class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        n1, n2 = len(word1), len(word2)

        @cache
        def dp(i1, i2):
            if i1 == n1 or i2 == n2:
                return max(n1-i1, n2-i2)
            
            if word1[i1] == word2[i2]:
                return dp(i1+1, i2+1)
            else:
                return 1 + min(dp(i1+1, i2), dp(i1, i2+1), dp(i1+1, i2+1))
        
        return dp(0, 0)