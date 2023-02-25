class Solution:
    def minWindow(self, s: str, t: str) -> str:
        required = Counter(t)
        t = set(t)
        start = 0
        shortest = [0, len(s)]
        for end in range(len(s)):
            if s[end] in t:
                required[s[end]] -= 1

            while all([val <= 0 for val in required.values()]):
                if end-start < shortest[1]-shortest[0]:
                    shortest = [start, end]
                
                if s[start] in t:
                    required[s[start]] += 1

                start += 1

        
        return s[shortest[0]: shortest[1]+1] if shortest[1] - shortest[0] < len(s) else ""