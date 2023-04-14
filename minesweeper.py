class Solution:
    def updateBoard(self, board: List[List[str]], click: List[int]) -> List[List[str]]:
        directions = list(itertools.product([-1, 0, 1], [-1, 0, 1]))
        isValid = lambda i, j: 0 <= i < len(board) and 0 <= j < len(board[0])

        def dfs(r, c):
            print(r, c)
            if board[r][c] == 'M':
                board[r][c] = 'X'
                return 
            
            adjMines = 0
            for r_step, c_step in directions:
                if (r_step, c_step) != (0, 0) and isValid(r+r_step, c+c_step): 
                    if board[r+r_step][c+c_step] == 'M':
                        adjMines += 1
                    
            
            if adjMines:
                board[r][c] = str(adjMines)
            else:
                board[r][c] = 'B'
                for r_step, c_step in directions:
                    if (r_step, c_step) != (0, 0) and isValid(r+r_step, c+c_step):
                        if board[r+r_step][c+c_step] != 'B':
                            dfs(r+r_step, c+c_step)
            
        dfs(*click)

        return board