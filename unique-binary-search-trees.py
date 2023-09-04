class Solution:
    def numTrees(self, n: int) -> int:
        memory = {0: 1}

        def uniquePath(n):
            if n in memory:
                return memory[n]
            
            res = 0
            for i in range(1, n+1):
                res += uniquePath(i-1) * uniquePath(n-i)
            
            memory[i] = res
            return res

        return uniquePath(n)