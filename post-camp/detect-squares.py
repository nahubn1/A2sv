class DetectSquares:

    def __init__(self):
        self.points = Counter()    

    def add(self, point: List[int]) -> None:
        self.points[tuple(point)] += 1
        
    def count(self, point: List[int]) -> int:
        cnt = 0
        for x, y in self.points: 
            if (x, y) != tuple(point) and abs(x - point[0]) == abs(y - point[1]):
                cnt += self.points[(x, point[1])] * self.points[(point[0], y)] * self.points[(x, y)]
                
    
        return cnt
        


# Your DetectSquares object will be instantiated and called as such:
# obj = DetectSquares()
# obj.add(point)
# param_2 = obj.count(point)