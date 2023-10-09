class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        n = len(gas)
        diff = [gas[i] - cost[i] for i in range(n)]

        minn = inf
        rSum = 0
        for num in diff:
            rSum += num
            minn = min(minn, rSum)
        if rSum < 0:
            return -1
            
        for i in range(n):
            if minn >= 0:
                return i
            
            minn -= diff[i]
        
        return -1