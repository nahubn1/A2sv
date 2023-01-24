from math import sqrt, ceil
class Solution:
    def judgeSquareSum(self, c: int) -> bool:
        ptr1 = 0
        ptr2 = ceil(sqrt(c))
        
        while ptr1 <= ptr2:
            if ptr1**2 + ptr2**2 < c:
                ptr1 += 1
            elif ptr1**2 + ptr2**2 > c:
                ptr2 -= 1
            else:
                return True

        return False