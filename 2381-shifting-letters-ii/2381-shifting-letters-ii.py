from itertools import accumulate
class Solution:
    @staticmethod
    def value(direction):
        return 1 if direction else -1

    def shiftingLetters(self, s: str, shifts: List[List[int]]) -> str:
        order = [0]*len(s)
        print(order)
        for start, end, direc in shifts:
            order[start] += self.value(direc)
            if end < len(s)-1: order[end+1] -= self.value(direc)
        
        print(order)
        order = list(accumulate(order))
        print(order)
        for i in range(len(s)):
            order[i] = chr(97+ ((ord(s[i])+order[i])-97)%26 )

        return ''.join(order)
            