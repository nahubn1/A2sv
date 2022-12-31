class Solution:
    @staticmethod
    def in_mat(pt, m, n):
        return 0 <= pt[0] < m and 0 <= pt[1] < n
    @staticmethod
    def move(x, y, direction):
        x += direction[0]
        y += direction[1]
        
    def findDiagonalOrder(self, mat: List[List[int]]) -> List[int]:
        m, n = len(mat), len(mat[0])
                
        NE = (-1, +1)
        SW = (+1, -1)
        East = (0, +1)
        
        direc = NE
        diag_trav = []
        x0, y0 = [-1, 0]
        x, y = [0 ,0]
        i = 0
        while x+y <= m+n-2:
            i += 1
            # print(x, y, direc)
            if self.in_mat((x, y), m, n):
                diag_trav.append(mat[x][y])
                # print(diag_trav)
            x0, y0 = x, y
            x = x0 + direc[0]
            y = y0 + direc[1]
            
            if self.in_mat((x0, y0), m, n) and not self.in_mat((x, y), m, n):
                # print('now', x0, y0)
                x += East[0]
                y += East[1]
                direc = SW if direc == NE else NE
                
        return diag_trav