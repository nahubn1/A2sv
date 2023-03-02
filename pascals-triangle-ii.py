class Solution:
    @staticmethod
    def sumPair(row):
        res = []
        for i in range(len(row)-1):
            res.append(row[i]+row[i+1])
        
        return res
            
    def getRow(self, rowIndex: int) -> List[int]:
        if rowIndex == 0:
            return [1]
        
        return [1, *self.sumPair(self.getRow(rowIndex-1)), 1]