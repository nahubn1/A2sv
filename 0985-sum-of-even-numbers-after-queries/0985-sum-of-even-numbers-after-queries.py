class Solution:
    @staticmethod
    def even(num):
        return num if num % 2 == 0 else 0
    def sumEvenAfterQueries(self, nums: List[int], queries: List[List[int]]) -> List[int]:
        sum_e = 0
        for num in nums:
            if num%2 == 0:
                sum_e += num
        
        answer = []
        for val, idx in queries:
            sum_e +=  self.even(nums[idx]+val) - self.even(nums[idx]) 
            nums[idx] += val
            answer.append(sum_e)
        
        return answer