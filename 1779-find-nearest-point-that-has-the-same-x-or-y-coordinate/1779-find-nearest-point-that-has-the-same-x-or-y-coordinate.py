from math import inf
class Solution:
    def nearestValidPoint(self, x: int, y: int, points: List[List[int]]) -> int:
        res = (-1, inf)
        for i, pt in enumerate(points):
            if pt[0] == x or pt[1] == y:
                manh_dist = abs(x-pt[0])+abs(y-pt[1])
                if manh_dist < res[1]:
                    res = (i, manh_dist)
        return res[0]
                    