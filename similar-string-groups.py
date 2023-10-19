class Solution:
    def numSimilarGroups(self, strs: List[str]) -> int:
        rep = {word: word for word in strs}
        
        def find(x):
            if x == rep[x]:
                return x
            
            rep[x] = find(rep[x])
            return rep[x]
        
        def union(u, v):
            repU = find(u)
            repV = find(v)

            if repU != repV:
                rep[repU] = repV
        
        def isSimilar(word1, word2):
            misMatch = 0

            for i in range(len(word1)):
                if word1[i] != word2[i]:
                    if misMatch < 2:
                        misMatch += 1
                    else:
                        return False
            
            return True

        for i in range(len(strs)):
            for j in range(i+1, len(strs)):
                if isSimilar(strs[i], strs[j]):
                    union(strs[i], strs[j])

        groups = 0
        for word in rep:
            if word == rep[word]:
                groups += 1
        
        return groups