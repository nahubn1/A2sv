class StockSpanner:

    def __init__(self):
        self.day = 0
        self.monStack = []
        self.span = {}
        self.cost = {}
    def next(self, price: int) -> int:
        self.day += 1
        self.span[self.day] = 1
        self.cost[self.day] = price
        while self.monStack and self.cost[self.monStack[-1]] <= self.cost[self.day]:
            self.span[self.day] += self.span[self.monStack.pop()]
        self.monStack.append(self.day)

        return self.span[self.day]
        


# Your StockSpanner object will be instantiated and called as such:
# obj = StockSpanner()
# param_1 = obj.next(price)