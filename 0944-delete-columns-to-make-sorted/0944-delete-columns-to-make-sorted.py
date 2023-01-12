class Solution:
    def minDeletionSize(self, strs: List[str]) -> int:
        deleted = 0
        for j in range(len(strs[0])):
            column_order = 0
            for i in range(len(strs)):
                if ord(strs[i][j]) < column_order:
                    print(chr(column_order), strs[i][j])
                    deleted += 1
                    break
                else:
                    column_order = ord(strs[i][j])
                    
        return deleted