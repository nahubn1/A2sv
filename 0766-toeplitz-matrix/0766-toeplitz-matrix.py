class Solution:
    def isToeplitzMatrix(self, matrix: List[List[int]]) -> bool:
        diag = {}
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                
                if i-j not in diag:
                    diag[i-j] = matrix[i][j]
                
                if matrix[i][j] != diag[i-j]:
                    return False
        
        return True