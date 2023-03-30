class Solution:
    def hammingDistance(self, x: int, y: int) -> int:
        diff = x^y
        count = 0

        while diff > 0:
            count += (diff&1)
            diff >>= 1

        return count