from itertools import cycle
class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        m, n = len(matrix), len(matrix[0])
        output = []
        directions = cycle([(0, 1), (1, 0), (0, -1), (-1, 0)])
        direc = next(directions)
        step = 0
        covered = set()
        pos = [0, -1]
        while step < m*n:
            pos[0] += direc[0]
            pos[1] += direc[1]
            output.append(matrix[pos[0]][pos[1]])
            covered.add(tuple(pos))
            step += 1

            if not(0 <= pos[0]+direc[0] < m) or not(0 <= pos[1]+direc[1] < n) or tuple([pos[0]+direc[0], pos[1]+direc[1]]) in covered:
                direc = next(directions)

        return output 

