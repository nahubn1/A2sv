class Solution:
    def tuplize(self, arr):
        return tuple([tuple(arr[0]), tuple(arr[1])])
    
    def swap(self, arr, r0, c0, r1, c1):
        arr[r0][c0], arr[r1][c1] = arr[r1][c1], arr[r0][c0]

    def initPos(self, board):
        for i in range(2):
            for j in range(3):
                if board[i][j] == 0:
                    return i, j

    def slidingPuzzle(self, board: List[List[int]]) -> int:
        winState = [[1,2,3], [4,5,0]]
        r_s, c_s = self.initPos(board)

        direc = [(1, 0), (0, 1), (-1, 0), (0, -1)]
        isValid = lambda r, c: 0 <= r < 2 and 0 <= c < 3

        que = deque([(r_s, c_s, board)])
        visited = set([self.tuplize(board)])
        step = 0
        while que:
            for _ in range(len(que)):
                r_0, c_0, board = que.popleft()
                if board == winState:
                    return step

                for r_step, c_step in direc:
                    r_new, c_new = r_0+r_step, c_0+c_step

                    if isValid(r_new, c_new):
                        board_new = deepcopy(board)
                        self.swap(board_new, r_0, c_0, r_new, c_new)

                        state = self.tuplize(board_new)
                        if state not in visited:
                            que.append((r_new, c_new, board_new))
                            visited.add(state)
            
            step += 1
        
        return -1