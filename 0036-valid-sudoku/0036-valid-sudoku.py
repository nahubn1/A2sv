class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        
        # row test
        for i in range(9):
            row_elements = set()
            for j in range(9):
                if board[i][j] == ".":
                    continue

                if  not(1 <= int(board[i][j]) <= 9) or board[i][j] in row_elements:
                    return False
                else:
                    row_elements.add(board[i][j])
        
        #column test       
        for j in range(9):
            column_elements = set()
            for i in range(9):
                if board[i][j] == ".":
                    continue

                if not(1 <= int(board[i][j]) <= 9) or board[i][j] in column_elements:
                    return False
                else:
                    column_elements.add(board[i][j])
                
        #sub-box test
        for i in range(0, 9, 3):
            for j in range(0, 9, 3):
                sub_box_elements = set()
                for r in range(i, i+3):
                    for c in range(j, j+3):
                        if board[r][c] == ".":
                            continue

                        if  not(1 <= int(board[r][c]) <= 9) or board[r][c] in sub_box_elements:
                            print(i, j, sub_box_elements, board[r][c])
                            return False
                        else:
                            sub_box_elements.add(board[r][c])

        #If it can pass all the tests
        return True