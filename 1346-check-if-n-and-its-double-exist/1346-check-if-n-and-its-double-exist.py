class Solution:
    def checkIfExist(self, arr: List[int]) -> bool:
        doubles = set()
        halfes = set()
        for i in arr:
            if 2*i in doubles or i in halfes:
                return True
            else:
                doubles.add(i)
                halfes.add(2*i)
        return False