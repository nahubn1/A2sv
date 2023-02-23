from collections import Counter
class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        n = len(s2)
        k = len(s1)

        target = Counter(s1)
        window = Counter(s2[:k])

        if window == target:
            return True

        for i in range(1, n-(k-1)):
            window[s2[i-1]] -= 1
            if window[s2[i-1]] == 0: del window[s2[i-1]]
            window[s2[i+k-1]] += 1
            
            if window == target:
                return True
        else:
            return False