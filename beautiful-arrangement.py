class Solution:
    def countArrangement(self, n: int) -> int:
        self.count = 0
        def backtrack(arr, bit):
            if len(arr) == n:
                self.count += 1
                return

            for i in range(1, n+1):
                if not bit&(1<<i):
                    
                    if (len(arr)+1)%i == 0 or i%(len(arr)+1) == 0:
                        backtrack(arr+[i], bit | (1<<i))

        backtrack([], 0)

        return self.count