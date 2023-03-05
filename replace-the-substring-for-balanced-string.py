class Solution:
    def balancedString(self, s: str) -> int:
        n = len(s)
        count = Counter(s)
        required = {}
        for char in count:
            if count[char]-(n//4) > 0:
                required[char] = count[char]-(n//4)

        print(required)
        
        if len(required) == 0:
            return 0

        start = 0
        minWindow = n
        found = defaultdict(int)
        for end in range(n):
            if s[end] in required:
                found[s[end]] += 1
            
            while all([found[char] >= required[char] for char in required]):
            
                minWindow = min(minWindow, end-start+1)
                if s[start] in required:
                    found[s[start]] -= 1

                start += 1

        return minWindow