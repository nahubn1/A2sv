#User function Template for python3
from collections import defaultdict
class Solution:
    def findOrder(self,alien_dict, N, K):
        
        graph = defaultdict(list)
        letter_collections = set(list(alien_dict[0]))
        for i in range(1, len(alien_dict)):
            ptr = 0
            word1, word2 = alien_dict[i-1], alien_dict[i]
            letter_collections  = letter_collections.union(list(word2))
            
            while ptr < min(len(word1), len(word2)):
                if word1[ptr] != word2[ptr]:
                    graph[word2[ptr]].append(word1[ptr])
                    break
                    
                ptr += 1
        
        color = defaultdict(int)
        def dfs(node):
            if color[node] == 1:
                return True
            
        
            if all([dfs(neighnor) for neighnor in graph[node]]):
                color[node] = 1 
                ans.append(node)
                return True
            
        ans = []
        for letter in letter_collections:
            dfs(letter)
            
        
        return ''.join(ans)