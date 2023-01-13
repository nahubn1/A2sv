class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        m, n = len(matrix), len(matrix[0])
        low = 0
        high = m*n - 1
        while low <= high:
            mid = (low + high)//2
            if target == matrix[mid//n][mid%n]:
                return True
                
            elif target > matrix[mid//n][mid%n]:
                low = mid+1
            else:
                high = mid-1
        else:
            return False