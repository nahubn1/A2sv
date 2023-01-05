from itertools import product
from copy import deepcopy
class Solution:
    def queensAttacktheKing(self, queens: List[List[int]], king: List[int]) -> List[List[int]]:
        queens = set(map(tuple, queens))
        directions = product([-1, 0, 1], [-1, 0, 1])
        killers = []
        for direc in directions:
            ray = deepcopy(king)
            
            if direc != (0, 0):
                while 0 <= ray[0]+direc[0] <= 8 and 0 <= ray[1]+direc[1] <= 8:
                    ray[0] += direc[0]
                    ray[1] += direc[1]
                    
                    if tuple(ray) in queens:
                        killers.append(tuple(ray))
                        break
        return killers