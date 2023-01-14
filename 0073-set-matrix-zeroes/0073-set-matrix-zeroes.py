class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        m, n = len(matrix), len(matrix[0])
        remove_row, remove_column = set(), set()
        for i in range(m):
            for j in range(n):
                if matrix[i][j] == 0:
                    remove_row.add(i)
                    remove_column.add(j)

        for row in remove_row:
            for j in range(n):
                matrix[row][j] = 0

        for column in remove_column:
            for i in range(m):
                matrix[i][column] = 0
