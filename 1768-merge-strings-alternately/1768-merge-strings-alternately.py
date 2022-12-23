class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        
        minLen = min(len(word1), len(word2))
        maxLen = max(len(word1), len(word2))
        extra = word1[minLen: maxLen] + word2[minLen: maxLen]
        
        merged = []
        for i in range(minLen):
            merged.append(word1[i])
            merged.append(word2[i])
            
        merged.extend(extra)
        return ''.join(merged)
            