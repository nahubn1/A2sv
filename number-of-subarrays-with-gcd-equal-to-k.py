class Solution:
    @staticmethod
    def gcd(a, b):
        if b==0:
            return a
        
        return gcd(b, a%b)

    def subarrayGCD(self, nums: List[int], k: int) -> int:
        count = 0

        for i in range(len(nums)):
            subGcd = nums[i]
            for j in range(i, len(nums)):
                subGcd = self.gcd(subGcd, nums[j])
                if subGcd == k:
                    count += 1

        return count