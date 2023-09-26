class Solution:
    def longestPalindromeSubseq(self, s: str) -> int:
        
        dp = defaultdict(int)
        for k in range(len(s)):
            for i in range(len(s)-k):
                if i == i+k:
                    dp[(i, i+k)] = 1
                elif s[i] == s[i+k]:
                    dp[(i, i+k)] = 2+dp[(i+1, i+k-1)]
                else:
                    dp[(i, i+k)] = max(dp[(i+1, i+k)], dp[(i, i+k-1)])
        
        return dp[(0, len(s)-1)]