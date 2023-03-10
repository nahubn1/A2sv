class Solution:
    def explore(self, start, arr):
        if start == self.n:
            if len(arr) >= 2:
                return True
            else:
                return
        
        for i in range(start, self.n):
            if not arr or arr[-1] - int(self.s[start: i+1]) == 1:
                arr.append(int(self.s[start: i+1]))
                found = self.explore(i+1, arr)
                arr.pop()

                if found:
                    return True

    def splitString(self, s: str) -> bool:
        self.s = s
        self.n = len(s)
        
        return self.explore(0, [])