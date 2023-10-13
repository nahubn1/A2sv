class Solution:
    def longestPrefix(self, s: str) -> str:
        lps = [0]*len(s)

        prevLps, i = 0, 1
        while i < len(s):
            if s[i] == s[prevLps]:
                lps[i] = prevLps + 1
                prevLps += 1
                i += 1
            elif prevLps > 0:
                prevLps = lps[prevLps-1]
            else:
                i += 1
        
        return s[:prevLps]