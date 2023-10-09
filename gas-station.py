class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        if sum(cost) > sum(gas):
            return -1
        n = len(gas)
        
        upper = [0]*n
        lower = [0]*n

        upper[0] = gas[0]
        for i in range(1, n):
            lower[i] = upper[i-1] - cost[i-1]
            upper[i] = lower[i] + gas[i]

            # print(i, upper, lower)
        
        lowest = -min(lower)
        for i in range(n):
            if gas[i] - upper[i] >= lowest:
                return i
        
        return -1