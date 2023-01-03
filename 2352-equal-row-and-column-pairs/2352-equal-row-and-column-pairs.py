from collections import Counter
import numpy as np
class Solution:
    def equalPairs(self, grid: List[List[int]]) -> int:
        count_r = Counter([])
        count_c = Counter([])
        
        grid = np.array(grid)
        
        for i in range(grid.shape[0]):
            count_r[hash(tuple(grid[i, :]))] += 1
            count_c[hash(tuple(grid[:, i]))] += 1
            
        pairs = 0
        for key in count_r:
            pairs += count_r[key]*count_c[key]
        
        return pairs
                
        