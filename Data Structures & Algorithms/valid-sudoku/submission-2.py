class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        
        checkcol = defaultdict(set)
        checkrow = defaultdict(set)
        checksub = defaultdict(set)

        for x in range(9):
            for y in range(9):
                if board[x][y] == ".":
                    continue
                
                if board[x][y] in checkrow[x] or \
                    board[x][y] in checkcol[y] or \
                    board[x][y] in checksub[(x//3,y//3)]:
                        return False
                
                checkcol[y].add(board[x][y])
                checkrow[x].add(board[x][y])
                checksub[(x//3,y//3)].add(board[x][y])
        
        return True