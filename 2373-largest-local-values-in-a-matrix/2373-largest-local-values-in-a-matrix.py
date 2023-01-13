class Solution:
    def largestLocal(self, grid: List[List[int]]) -> List[List[int]]:
        n = len(grid)
        maxLocal = [[0]*(n-2) for i in range(n-2)]

        for i in range(n-2):
            for j in range(n-2):

                for k in range(i, i+3):
                    for l in range(j, j+3):
                        maxLocal[i][j] = max(grid[k][l], maxLocal[i][j])

        return maxLocal

        return []