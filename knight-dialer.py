class Solution:
    def knightDialer(self, n: int) -> int:
        moves = {0: [6, 4], 1: [6, 8],  2: [9, 7], 
                 3: [8, 4], 4: [0, 3, 9],  5: [],
                 6: [0, 1, 7], 7: [6, 2], 
                 8: [1, 3], 9: [2, 4],  
                }

        row = [1]*10
        lastRow = row.copy()
        for i in range(1, n):
            row = [0]*10

            for j in range(10):
                for k in moves[j]:
                    row[k] += lastRow[j]
            
            lastRow = row.copy()
        
        
        return sum(row) % (10**9 + 7)