class Solution:
    def solve(self, board: List[List[str]]) -> None:
        
        ROWS, COLS = len(board), len(board[0])
        visited = set()

        def checkInvalid(r,c):
            directions = [[1,0],[-1,0],[0,1],[0,-1]]

            visited.add((r,c))
            queue = deque([(r,c)])

            while queue:
                row, col = queue.popleft()

                for rd, cd in directions:
                    nr, nc = row + rd, col + cd

                    if(
                        nr in range(ROWS) and
                        nc in range(COLS) and
                        board[nr][nc] == "O" and
                        (nr,nc) not in visited
                    ):
                        visited.add((nr,nc))
                        queue.append((nr,nc))

        for row in range(ROWS):
            col = 0
            while col in range(COLS): 
                if(
                    board[row][col] == "O"
                ):
                    checkInvalid(row,col)

                if(
                    row in range(1, ROWS - 1) and
                    col == 0
                ):
                    col = COLS - 1
                else:
                    col += 1

        for row in range(1, ROWS - 1):
            for col in range(1, COLS - 1):
                if(
                    board[row][col] == "O" and
                    (row,col) not in visited
                ):
                    board[row][col] = "X"