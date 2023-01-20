class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        nums.sort(reverse=True)
        nums = list(map(str, nums))
        outPut = []
        for i in range(len(nums)):
            pos = i
            while pos > 0 and int(nums[i]+outPut[pos-1])>int(outPut[pos-1]+nums[i]):
                pos -= 1
            outPut.insert(pos, nums[i])
        return str(int(''.join(outPut)))