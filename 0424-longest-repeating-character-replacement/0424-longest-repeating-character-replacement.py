class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        start = 0
        mostFreq = 0
        hashmap = defaultdict(int)
        longest = 0
        
        for end in range(len(s)):
            hashmap[s[end]] += 1
            mostFreq = max(mostFreq, hashmap[s[end]])
            
            while (end-start+1) - mostFreq > k:

                hashmap[s[start]] -= 1
                start += 1
                
            longest = end-start+1
            
        return longest