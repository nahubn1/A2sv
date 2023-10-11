class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        m, n = len(haystack), len(needle)
        if n > m: return -1
        window = 0
        target = 0
        for i in range(n):
            window += (ord(haystack[i])-96)*(27**i)
            target += (ord(needle[i])-96)*(27**i)
        

        for i in range(m-n):
            if window == target:
                return i

            window -= (ord(haystack[i])-96)
            window //= 27
            window += (ord(haystack[i+n])-96) * (27**(n-1))
        
        return m-n if window == target else -1