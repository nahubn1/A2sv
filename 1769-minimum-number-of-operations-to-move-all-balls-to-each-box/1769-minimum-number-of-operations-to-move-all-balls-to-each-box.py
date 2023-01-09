class Solution:
    def minOperations(self, boxes: str) -> List[int]:
        n = len(boxes)
        
        balls_before = balls_after = 0

        moves_right = []
        for i in range(n):
            if moves_right:
                moves_right.append(moves_right[-1]+balls_before)
            else:
                moves_right.append(balls_before)
                
            if boxes[i] == '1':
                balls_before += 1
                
        moves_left = []
        for i in range(n-1, -1, -1):                
            if moves_left:
                moves_left.append(moves_left[-1]+balls_after)
            else:
                moves_left.append(balls_after)
                
            if boxes[i] == '1':
                balls_after += 1
                
        moves = []
        for i in range(n):
            moves.append(moves_right[i]+moves_left[n-i-1])
            
        return moves