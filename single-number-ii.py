class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        ones = 0
        twos = 0
        for num in nums:
            ones = ~twos & (ones^num)
            twos = ~ones & (twos^num)

        return ones