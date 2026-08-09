class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        
        col_check = set()
        row_check = set()
        posdiag_check = set()
        negdiag_check = set()

        res = []
        board = [["."] * n for i in range(n)]

        def backtrack(r):
            if r == n:
                copy = ["".join(row) for row in board]
                res.append(copy)
                return

            for c in range(n):
                if c in col_check or \
                    (r + c) in posdiag_check or \
                    (r - c) in negdiag_check:
                        continue
                
                col_check.add(c)
                posdiag_check.add(r + c)
                negdiag_check.add(r - c)
                board[r][c] = "Q"

                backtrack(r + 1)

                col_check.remove(c)
                posdiag_check.remove(r + c)
                negdiag_check.remove(r - c)
                board[r][c] = "."


        backtrack(0)

        return res
