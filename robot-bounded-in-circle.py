class Solution:
    def isRobotBounded(self, instructions: str) -> bool:
        pos = (0, 0, 0)
        
        direc = {0: (1, 0), 1: (0, -1), 2: (-1, 0), 3: (0, 1)}

        for i in range(4):
            for inst in instructions:
                x, y, o = pos
                if inst == 'G':
                    x += direc[o][0]
                    y += direc[o][1]
                elif inst == 'L':
                    o += 1
                else:
                    o -= 1
                
                pos = (x, y, o%4)

            if pos == (0, 0, 0):
                return True
        
        return False