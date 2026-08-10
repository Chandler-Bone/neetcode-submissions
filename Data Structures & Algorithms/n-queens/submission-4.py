class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        
        col_check = set()
        posdiag_check = set()
        negdiag_check = set()

        res = []
        board = [["."] * n for i in range(n)]

        def backtrack(row):
            if row == n:
                copy = ["".join(i) for i in board]
                res.append(copy)

            for col in range(n):
                if col in col_check or \
                    row + col in posdiag_check or \
                    row - col in negdiag_check:
                        continue
                
                col_check.add(col)
                posdiag_check.add(row + col)
                negdiag_check.add(row - col)
                board[row][col] = "Q"

                backtrack(row + 1)

                col_check.remove(col)
                posdiag_check.remove(row + col)
                negdiag_check.remove(row - col)
                board[row][col] = "."

        backtrack(0)

        return res