class Solution:
    def calculateMinimumHP(self, dungeon: List[List[int]]) -> int:
        m, n = len(dungeon), len(dungeon[0])
        for row in dungeon: row.append(-inf)
        dungeon.append([-inf]*(n+1))
        dungeon[m-1][n] = dungeon[m][n-1] = 0

        for i in range(m-1, -1, -1):
            for j in range(n-1, -1, -1):
                dungeon[i][j] = min(0, max(dungeon[i+1][j], dungeon[i][j+1])+dungeon[i][j])
        
        return abs(dungeon[0][0])+1