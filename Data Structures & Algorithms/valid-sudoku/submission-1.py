class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
         for i in range(9):
            row_set = set()
            col_set = set()
            for j in range(9):
                if board[i][j] in row_set or board[j][i] in col_set:
                    return False
                if board[i][j] != '.':
                    row_set.add(board[i][j])
                if board[j][i] != '.':
                    col_set.add(board[j][i])

        # Check sub-boxes
         for i in range(0, 9, 3):
            for j in range(0, 9, 3):
                sub_box_set = set()
                for x in range(3):
                    for y in range(3):
                        if board[i+x][j+y] in sub_box_set:
                            return False
                        if board[i+x][j+y] != '.':
                            sub_box_set.add(board[i+x][j+y])

         return True

