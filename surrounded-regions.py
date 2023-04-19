class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        isValid = lambda i, j: 0 <= i < len(board) and 0 <= j < len(board[0])
        direc = [(1, 0), (0, 1), (-1, 0), (0, -1)]
        m, n = len(board), len(board[0])
        def dfs(r, c):
            board[r][c] = 'Z'

            for r_step, c_step in direc:
                if isValid(r+r_step, c+c_step) and board[r+r_step][c+c_step] == 'O':
                    dfs(r+r_step, c+c_step)
                
            
        for i in range(m):
            if board[i][0] =='O':
                dfs(i, 0)
            if board[i][n-1] =='O':
                dfs(i, n-1)
        
        for j in range(n):
            if board[0][j] =='O':
                dfs(0, j)
            if board[m-1][j] =='O':
                dfs(m-1, j)

        for i in range(m):
            for j in range(n):
                if board[i][j] == 'Z':
                    board[i][j] = 'O'
                elif board[i][j] == 'O':
                    board[i][j] = 'X'