class Solution:
    def repeatedStringMatch(self, a: str, b: str) -> int:
        m, n = len(a), len(b)

        lps = [0]*n
        prevLps, i = 0, 1
        while i < n:
            if b[i] == b[prevLps]:
                lps[i] = 1 + prevLps
                prevLps += 1
                i += 1
            elif prevLps > 0:
                prevLps = lps[prevLps-1]
            else:
                i += 1
        
        repeat = 1
        i, j = 0, 0
        visited = set()

        while (i, j) not in visited:
            visited.add((i, j))
            if a[i] == b[j]:
                i, j = i+1, j+1
            elif j > 0:
                j = lps[j-1]
            else:
                i += 1
            
            if j == n:
                return repeat

            if i == m:
                repeat += 1
                i = 0

        return -1