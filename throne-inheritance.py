class ThroneInheritance:

    def __init__(self, kingName: str):
        self.king = kingName
        self.familiyTree = defaultdict(list)
        self.familiyTree[kingName] = []
        
        self.alive = defaultdict(lambda: True)

    def birth(self, parentName: str, childName: str) -> None:
        self.familiyTree[parentName].append(childName)

    def death(self, name: str) -> None:
        self.alive[name] = False

    def getInheritanceOrder(self) -> List[str]:
        curOrder = []

        def dfs(person):
            if self.alive[person]:
                curOrder.append(person)

            for child in self.familiyTree[person]:
                dfs(child)
        
        dfs(self.king)
        return curOrder
        


# Your ThroneInheritance object will be instantiated and called as such:
# obj = ThroneInheritance(kingName)
# obj.birth(parentName,childName)
# obj.death(name)
# param_3 = obj.getInheritanceOrder()