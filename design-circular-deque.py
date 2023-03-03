class MyCircularDeque:

    def __init__(self, k: int):
        self.k = k
        self.deque = [-1]*k
        self.start = 0
        self.end = 0
        
    def insertFront(self, value: int) -> bool:
        if not self.isFull():
            self.deque[(self.start-1)%self.k] = value
            self.start = (self.start-1)%self.k 
            # self.printdeque()
            return True
        else:
            # self.printdeque()
            return False

    def insertLast(self, value: int) -> bool:
        if not self.isFull():
            self.deque[self.end] = value
            self.end = (self.end+1)%self.k 
            # self.printdeque()
            return True
        else:
            # self.printdeque()
            return False
        

    def deleteFront(self) -> bool:
        if self.deque[self.start] != -1:
            self.deque[self.start] = -1
            self.start = (self.start+1)%self.k
            # self.printdeque()
            return True
        else:
            # self.printdeque()
            return False

    def deleteLast(self) -> bool:
        if self.deque[(self.end-1)%self.k] != -1:
            self.deque[(self.end-1)%self.k] = -1
            self.end = (self.end-1)%self.k
            # self.printdeque()
            return True
        else:
            self.printdeque()
            return False


    def getFront(self) -> int:
        return self.deque[self.start]

    def getRear(self) -> int:
        return self.deque[(self.end-1)%self.k]

    def isEmpty(self) -> bool:
        if self.start == self.end and self.deque[self.end] == -1:
            return True
        else:
            return False

    def isFull(self) -> bool:
        if self.start == self.end and self.deque[self.end] != -1:
            return True
        else:
            return False
            
    def printdeque(self):
        print('-----')
        print('s =', self.start, 'e =', self.end)
        print(self.deque)
        print('-----')


# Your MyCircularDeque object will be instantiated and called as such:
# obj = MyCircularDeque(k)
# param_1 = obj.insertFront(value)
# param_2 = obj.insertLast(value)
# param_3 = obj.deleteFront()
# param_4 = obj.deleteLast()
# param_5 = obj.getFront()
# param_6 = obj.getRear()
# param_7 = obj.isEmpty()
# param_8 = obj.isFull()