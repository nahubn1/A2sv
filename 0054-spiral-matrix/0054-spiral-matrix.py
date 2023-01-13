from itertools import cycle
import numpy as np
class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        mat = np.array(matrix)
        output = []
        directions = cycle(['R', 'D', 'L', 'U'])
        m, n = mat.shape
        for drcn in directions:
            if drcn == 'R':
                output += list(mat[0, :])
                mat = mat[1:, :]
            elif drcn == 'D':
                output += list(mat[:,-1])
                mat = mat[:, :-1]
            elif drcn == 'L':
                output += list(reversed(mat[-1, :]))
                mat = mat[:-1, :]
            else:
                output += list(reversed(mat[:,0]))
                mat = mat[:, 1:]
            if len(output) == m*n:
                return output