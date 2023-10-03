class Solution:
    def twoCitySchedCost(self, costs: List[List[int]]) -> int:
        
        minCost = 0
        diff = []
        for costA, costB in costs:
            minCost += costA
            diff.append(costB-costA)
        
        diff.sort()

        return minCost + sum(diff[:len(costs)//2])