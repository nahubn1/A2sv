class Solution:
    @staticmethod
    def gridize(X, n):
        r = (n-1) - (X-1)//n
        if ((n-1) - r) % 2 == 0:
            c = (X-1)%n
        else:
            c = (n-1) - (X-1)%n
        
        return r, c

    def snakesAndLadders(self, board: List[List[int]]) -> int:
    
        n = len(board)
        que = deque([1])
        visited = set([1])

        step = 0
        while que:
            lev_len = len(que)
            for i in range(lev_len):
                curr = que.popleft()
                if curr == n**2:
                    return step

                for next_ in range(curr+1, min(curr+6, n**2)+1):
                    r, c = self.gridize(next_, n)
                    if board[r][c] != -1:
                        next_  = board[r][c]
                    
                    if next_ not in visited:
                        que.append(next_)
                        visited.add(next_)
        
            step += 1
        
        return -1