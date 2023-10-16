class RandomizedSet:

    def __init__(self):
        self.idx = {}
        self.data = []

    def insert(self, val: int) -> bool:
        if val not in self.idx:
            self.data.append(val)
            self.idx[val] = len(self.data)-1
            return True
        else:
            return False
        

    def remove(self, val: int) -> bool:
        if val in self.idx:
            i = self.idx[val]

            self.data[i], self.data[-1] = self.data[-1], self.data[i]
            self.idx[self.data[i]] = i
            self.data.pop()
            del self.idx[val]
            return True
        else:
            return False
            
        

    def getRandom(self) -> int:
        return random.choice(self.data) 
        


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()