from itertools import cycle
class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        m, n = len(matrix), len(matrix[0])
        output = []
        directions = cycle([(0, 1), (1, 0), (0, -1), (-1, 0)])
        direc = next(directions)
        step = 0
        i, j = 0, 0
        while step < m*n:

            if not(0 <= i+direc[0] < m) or not(0 <= j+direc[1] < n) or matrix[i+direc[0]][j+direc[1]] == '#':
                direc = next(directions)
            
            output.append(matrix[i][j])
            matrix[i][j] = '#'
            
            i += direc[0]
            j += direc[1]
            step += 1
                                                                                                

        return output 
               


