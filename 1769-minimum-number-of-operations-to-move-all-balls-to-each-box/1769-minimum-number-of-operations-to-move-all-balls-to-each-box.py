class Solution:
    def minOperations(self, boxes: str) -> List[int]:
        n = len(boxes)
        
        balls_before = []
        for i in range(n):
            if balls_before:
                balls_before.append(balls_before[-1]+int(boxes[i-1]))
            else:
                balls_before.append(0)
        
        balls_after = []
        for i in range(n-1, -1, -1):
            if balls_after:
                balls_after.append(balls_after[-1]+int(boxes[i+1]))
            else:
                balls_after.append(0)
        
        moves_right = []
        for i in range(n):
            if moves_right:
                moves_right.append(moves_right[-1]+balls_before[i])
            else:
                moves_right.append(balls_before[i])
                
        moves_left = []
        for i in range(n-1, -1, -1):
            if moves_left:
                moves_left.append(moves_left[-1]+balls_after[n-i-1])
            else:
                moves_left.append(balls_after[n-i-1])
                
        moves = []
        for i in range(n):
            moves.append(moves_right[i]+moves_left[n-i-1])
            
        return moves