class Solution:
    def racecar(self, target: int) -> int:
        que = deque([(0, 1)])
        visited = set([(0, 1)])
        count = 0
        while True:
            lev_len = len(que)
            for _ in range(lev_len):

                pos, speed = que.popleft()

                if pos == target:
                    return count
                
                newSpeed = 2*speed
                if -2*target < speed+pos < 2*target and (pos+speed, newSpeed) not in visited: 
                    que.append((pos+speed, newSpeed))
                    visited.add((pos+speed, newSpeed))

                newSpeed = 1 if speed < 0 else -1
                if (pos, newSpeed) not in visited: 
                    que.append((pos, newSpeed))
                    visited.add((pos, newSpeed))
            
            count += 1