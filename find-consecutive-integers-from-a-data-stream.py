class DataStream:

    def __init__(self, value: int, k: int):
        self.value = value
        self.k = k
        self.deque = deque([-1]*k)
        self.valCount = 0

    def consec(self, num: int) -> bool:
        self.deque.append(num)
        if num == self.value: self.valCount += 1
        if self.deque.popleft() == self.value: self.valCount -= 1
        return self.valCount == self.k


# Your DataStream object will be instantiated and called as such:
# obj = DataStream(value, k)
# param_1 = obj.consec(num)