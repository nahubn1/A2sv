class Solution:
    def countMaxOrSubsets(self, nums: List[int]) -> int:
        self.maxOr = 0
        for num in nums:
            self.maxOr |= num

        self.count = 0
        def backtrack(bit, start):
            subOr = 0
            for i in range(bit.bit_length()):
                if bit & (1<<i):
                    subOr |= nums[i]
            
            if subOr == self.maxOr:
                self.count += 1

            for i in range(start, len(nums)):
                backtrack(bit | (1<<i), i+1)
        
        backtrack(0, 0)

        return self.count