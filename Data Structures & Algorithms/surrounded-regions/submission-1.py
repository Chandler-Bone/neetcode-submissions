class Solution:
    def solve(self, board: List[List[str]]) -> None:
        
        ROWS, COLS = len(board), len(board[0])
        visited = set()

        def attemptCapture(r,c):
            directions = [[1,0],[-1,0],[0,1],[0,-1]]

            region = [(r,c)]
            visited.add((r,c))
            queue = deque([(r,c)])
            invalid_region = False

            while queue:
                row, col = queue.popleft()

                if(
                    row == 0 or row == ROWS - 1 or
                    col == 0 or col == COLS - 1
                ):
                    invalid_region = True

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
                        region.append((nr,nc))

            if not invalid_region:
                for row, col in region:
                    board[row][col] = "X"

        for row in range(ROWS):
            for col in range(COLS):
                if(
                    board[row][col] == "O" and
                    (row,col) not in visited
                ):
                    attemptCapture(row,col)