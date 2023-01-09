class Solution:
    def minOperations(self, boxes: str) -> List[int]:
        n = len(boxes)
        
        balls_before = balls_after = 0
        moves_right = moves_left = 0
        
        moves = [0]*n
        for i in range(n):
            moves_right += balls_before
            moves_left += balls_after
            
            moves[i] += moves_right
            moves[n-i-1] += moves_left
            
            if boxes[i] == '1':
                balls_before += 1
            if boxes[n-i-1] == '1':
                balls_after += 1
            
        return moves