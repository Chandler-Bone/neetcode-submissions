class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        for x in range(0,9,1):
            check_set_rows = set()
            check_set_cols = set()

            for y in range(0,9,1):
                row_val = board[x][y]
                if row_val != "." and row_val in check_set_rows:
                    return False
                check_set_rows.add(board[x][y])
                
                col_val = board[y][x]
                if col_val != "." and col_val in check_set_cols:
                    return False
                check_set_cols.add(board[y][x])

            
        x = 0
        y = 0
        sub_x = 0
        sub_y = 0
        
        while sub_y < 3:
            check_sub = set()
            for x in range(0,3,1):
                for y in range(0,3,1):
                    xreal = x + (sub_x * 3)
                    yreal = y + (sub_y * 3)
                    if board[xreal][yreal] != "." and board[xreal][yreal] in check_sub:
                        return False
                    check_sub.add(board[xreal][yreal])
            
            sub_x += 1

            if sub_x == 3:
                sub_x = 0
                sub_y += 1


        return True

