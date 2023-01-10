class Solution:
    def lengthOfLongestSubstring(self, s):
        Set = set()
        maxLen = 0
        start = 0
        
        for end in range(len(s)):
            
            while s[end] in Set:
                Set.remove(s[start])
                start += 1
                
            Set.add(s[end])    
            maxLen = max(maxLen, end - start + 1)    
            
        return maxLen
            