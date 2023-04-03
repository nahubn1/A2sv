class Solution:
    @staticmethod
    def gcd(a, b):
        if b == 0:
            return a

        return gcd(b, a%b)

    def findGCD(self, nums: List[int]) -> int:
        return gcd(max(nums), min(nums))