class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        cols = defaultdict(set)
        rows = defaultdict(set)
        squares = defaultdict(set)  

        for r in range(9):
            for c in range(9):
                if board[r][c] == ".":
                    continue
                if (
                    board[r][c] in rows[r]
                    or board[r][c] in cols[c]
                    or board[r][c] in squares[(r // 3, c // 3)]):
                    return False
                cols[c].add(board[r][c])
                rows[r].add(board[r][c])
                squares[(r // 3, c // 3)].add(board[r][c])

        return True

'''
class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:

        cols = defaultdict(set)
        rows = defaultdict(set)
        squares = defaultdict(set)

        diag = set()
        anti_diag = set()

        for r in range(9):
            for c in range(9):

                if board[r][c] == ".":
                    continue

                val = board[r][c]

                if (
                    val in rows[r]
                    or val in cols[c]
                    or val in squares[(r // 3, c // 3)]
                    or (r == c and val in diag)
                    or (r + c == 8 and val in anti_diag)
                ):
                    return False

                rows[r].add(val)
                cols[c].add(val)
                squares[(r // 3, c // 3)].add(val)

                if r == c:
                    diag.add(val)

                if r + c == 8:
                    anti_diag.add(val)

        return True

    '''


        