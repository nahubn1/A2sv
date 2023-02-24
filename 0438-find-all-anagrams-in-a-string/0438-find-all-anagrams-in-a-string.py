from collections import Counter
class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        n = len(s)
        k = len(p)

        anagrams = []
        window = Counter(s[:k])
        required = Counter(p)
        
        if window == required: anagrams.append(0)

        for i in range(k, n):
           
            window[s[i-k]] -= 1
            if window[s[i-k]] == 0: del window[s[i-k]]

            window[s[i]] += 1

            if window == required:
                anagrams.append(i-k+1)

        return anagrams
            