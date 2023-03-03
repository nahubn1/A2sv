class Solution:
    @staticmethod
    def invert_reverse(s):
        res = []
        for char in s:
            res.append("0" if char == "1" else "1")
        res.reverse()
        return ''.join(res)

    def formBinary(self, n):
        if n == 1:
            return "0"
        else:
            return self.formBinary(n-1) + "1" + self.invert_reverse(self.formBinary(n-1))

    def findKthBit(self, n: int, k: int) -> str:
        return self.formBinary(n)[k-1]