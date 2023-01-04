import numpy as np
class Solution:
    def printVertically(self, s: str) -> List[str]:
        matrix = []
        for word in s.split():
            matrix.append(list(word))
        
        longest_row = len(max(matrix, key=len))
        output = ['']*longest_row
        empty = [0]*longest_row
        for row in matrix:
            n = len(row)
            for j in range(longest_row):
                if j < n:
                    output[j] += (' '*empty[j] + row[j])
                    empty[j] = 0
                else:
                    empty[j] += 1
               
        return output