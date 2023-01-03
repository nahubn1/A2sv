class Solution:
    def minDeletionSize(self, strs: List[str]) -> int:
        deleted = set()
        m, n = len(strs), len(strs[0])
        last_ascii = [96]*n
        for string in strs:
            for i in range(n):
                if i not in deleted:
                    if ord(string[i]) < last_ascii[i]:
                        deleted.add(i)
                    else:
                        last_ascii[i] = ord(string[i])
        
        return len(deleted)