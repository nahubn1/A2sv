class Solution:
    def openLock(self, deadends: List[str], target: str) -> int:
        deadend = set(deadends)
        if "0000" in deadends:
            return -1

        def bfs():
            que = deque(["0000"])
            visited = set(["0000"])
            step = 0

            while que:

                lev_len = len(que)
                for _ in range(lev_len):

                    key = que.popleft()
                    if key == target:
                        return step

                    for i in range(8):
                        if i < 4:
                            newKey = key[:i] + str((int(key[i]) + 1)%10) + key[i+1:]
                        else:
                            newKey = key[:i-4] + str((int(key[i-4]) - 1)%10) + key[(i+1)-4:]

                        if newKey not in deadend and newKey not in visited:
                            que.append(newKey)
                            visited.add(newKey)
                
                step += 1
            
            return -1
        
        return bfs()