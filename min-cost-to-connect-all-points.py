class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        n = len(points)
        closestPoints = {}
        manDist = lambda a, b: abs(points[a][0] - points[b][0]) + abs(points[a][1] - points[b][1])
        for i in range(n):
            closestPoints[i] = []
            for j in range(n):
                if i != j:
                    closestPoints[i].append(j)
            
            closestPoints[i].sort(key = lambda x: manDist(x, i), reverse = True)
    
        

        connected = set([0])
        unconnected = set(range(1, n))

        totalCost = 0
        while len(connected) < n:
            
            minDist = (inf, -1, -1)
            for p1 in connected:
                p2 = closestPoints[p1].pop() 

                while p2 in connected:
                    p2 = closestPoints[p1].pop()
                
                if manDist(p1, p2) < minDist[0]:
                    dist, pt1, pt2 = minDist
                    if pt1 != -1: closestPoints[pt1].append(pt2) 
                    minDist = (manDist(p1, p2),  p1, p2)
                else:
                    closestPoints[p1].append(p2) 

            cost, point = minDist[0], minDist[2]

            totalCost += cost
            connected.add(point)
            unconnected.remove(point)
    
        return totalCost