class Solution:
    def hasAlternatingBits(self, n: int) -> bool:
        i = n.bit_length()-1
        expect = 1
        while i >= 0:
            if (n & (1<<i) != 0) != expect:
                return False

            i -= 1
            expect = not expect

        return True