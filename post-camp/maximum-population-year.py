class Solution:
    def maximumPopulation(self, logs: List[List[int]]) -> int:
        
        maxPop = (0, -1)
        for year in range(2050, 1949, -1):
            pop = 0
            for birth, death in logs:

                if birth <= year < death:
                    pop += 1
        
            maxPop = max(maxPop, (pop, -year))
        
        return -maxPop[1]