from typing import List
from collections import defaultdict

class Solution:
    #Function to detect cycle in an undirected graph.
	def isCycle(self, V: int, adj: List[List[int]]) -> bool:
	    
	    
		def dfs(parent, curr, same):
            
            if curr in same:
                return True
            
            visited.add(curr)
            same.add(curr)
        
            for neighbor in adj[curr]:
                
                if neighbor != parent:
                    if dfs(curr, neighbor, same):
                        return True
            
            return False

        visited = set()
        for i in range(V):
            if i not in visited:
                if dfs(-1, i, set()):
                    return True
        
        return False