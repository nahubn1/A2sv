class Solution:
    def champagneTower(self, poured: int, query_row: int, query_glass: int) -> float:

        row = [poured]
        depth = 0
        excess = poured
        while excess > 0:
            
            next_row = [0]*(len(row)+1)
            for i, vol in enumerate(row):
                excess -= min(1, vol)
                if depth == query_row and i == query_glass:
                    return min(1, vol)

                next_row[i] += max(0, (vol - 1) / 2)
                next_row[i+1] += max(0, (vol -1) / 2)
            
            row = next_row
            depth += 1
        
        return 0