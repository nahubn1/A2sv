class Solution:
    def maxRunTime(self, n: int, batteries: List[int]) -> int:
        batteries.sort()
        live = batteries[-n:]
        extra = sum(batteries[:-n])

        addedTime = 0
        for i in range(1, n):
            if extra >= i*(live[i] - live[i-1]):
                extra -= i*(live[i] - live[i-1])
            else:
                return live[i-1] + extra // i
            
        return live[-1] + extra // n