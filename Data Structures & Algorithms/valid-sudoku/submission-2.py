class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        #Check row or column
        
        for i in range(9):
            row_set = set()
            column_set = set()
            for j in range(9):
                if board[i][j] in row_set or board[j][i] in column_set:
                    return False
                if board[i][j] != ".":
                    row_set.add(board[i][j])
                if board[j][i] != ".":
                    column_set.add(board[j][i])

        #Check subrows
        
        for i in range(0,9,3):
            for j in range(0,9,3):
                sub_box_set = set()
                for x in range(3):
                    for y in range(3):
                        if board[i+x][j+y] in sub_box_set:
                            return False
                        if board[i+x][j+y] != ".":
                            sub_box_set.add(board[i+x][j+y])
        return True




        