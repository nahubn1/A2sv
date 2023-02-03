from math import ceil
class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows == 1:
            return s
        
        k = (numRows)*ceil(len(s)/(2*numRows-2))
        matrix = []
        for i in range(numRows):
            row = []
            for j in range(k):
                row.append(0)
            matrix.append(row)
        
        down = True
        i, j = 0, 0
        for char in s:
            matrix[i][j] = char

                
            if down and i == numRows-1:
                down = not down
            
            if not down and i == 0:
                down = not down
                
            if down:
                i += 1
            else:
                i -= 1
                j += 1
                
        output = []
        for i in range(numRows):
            for j in range(k):
                if matrix[i][j]:
                    output.append(matrix[i][j])
                    
        return ''.join(output)
                
                
                