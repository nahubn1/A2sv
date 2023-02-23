class NumArray:

    def __init__(self, nums: List[int]):
        self.preSum = list(accumulate(nums))
    def sumRange(self, left: int, right: int) -> int:
        return self.preSum[right] - self.preSum[left-1] if left>0 else self.preSum[right]


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(left,right)