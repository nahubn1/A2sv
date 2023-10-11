class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        m, n = len(s1), len(s2)

        if m > n:
            return False

        index = lambda char: ord(char)-96
        target = Counter(s1)

        window = Counter(s2[:m])

        for i in range(n-m):
            if window == target:
                return True
            
            window[s2[i]] -= 1
            window[s2[i+m]] += 1 
        
        return window == target