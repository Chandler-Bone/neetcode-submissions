class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        check_row = defaultdict(set)
        check_col = defaultdict(set)
        check_sub = defaultdict(set)

        for x in range(9):
            for y in range(9):
                if board[x][y] == ".":
                    continue

                if board[x][y] in check_row[y] \
                    or board[x][y] in check_col[x] \
                    or board[x][y] in check_sub[(x//3,y//3)]:
                        return False

                check_row[y].add(board[x][y])
                check_col[x].add(board[x][y])
                check_sub[(x//3,y//3)].add(board[x][y])
        
        return True