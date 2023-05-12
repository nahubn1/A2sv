from sortedcontainers import SortedList
class MedianFinder:

    def __init__(self):
        self.data = SortedList()

    def addNum(self, num: int) -> None:
        self.data.add(num)

    def findMedian(self) -> float:
        n = len(self.data)
        if len(self.data)%2 == 1:
            return self.data[n//2]
        else:
            return (self.data[n//2 - 1] + self.data[n//2])/2
        


# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()