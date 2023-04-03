class Solution:
    def maxProduct(self, words: List[str]) -> int:
        letters = defaultdict(int)
        for word in words:
            for char in word:
                letters[word] |= 1<<(ord(char)-97)


        maxCount = 0
        for i in range(len(words)):
            for j in range(i+1, len(words)):
                if letters[words[i]] & letters[words[j]] == 0:
                    maxCount = max(maxCount, len(words[i])*len(words[j]))
        
        return maxCount