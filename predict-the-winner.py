class Solution:
    def minimax(self, start, end, turn, score):
        if start == end:
            score[turn] += self.nums[start]
            return score[0]-score[1]

        p1Score, p2Score = score
        if turn == 0:
            return max(self.minimax(start+1, end, not turn, [p1Score+self.nums[start], p2Score]), self.minimax(start, end-1, not turn, [p1Score+self.nums[end], p2Score]))
        else:
            return min(self.minimax(start+1, end, not turn, [p1Score, p2Score+self.nums[start]]), self.minimax(start, end-1, not turn, [p1Score, p2Score+self.nums[end]]))
        


    def PredictTheWinner(self, nums: List[int]) -> bool:
        self.nums = nums
        if self.minimax(0, len(nums)-1, 0, [0, 0]) >= 0:
            return True
        else:
            return False