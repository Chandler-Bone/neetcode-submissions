class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        
        ROWS, COLS = len(grid), len(grid[0])
        queue = deque()
        directions = [[1,0],[-1,0],[0,1],[0,-1]]

        for row in range(ROWS):
            for col in range(COLS):
                if grid[row][col] == 0:
                    queue.append((row,col))

        while queue:
            row, col = queue.popleft()

            for rd, cd in directions:
                nr, nc = row + rd, col + cd

                if (
                    nr in range(ROWS) and
                    nc in range(COLS) and
                    grid[row][col] + 1 < grid[nr][nc]
                ):
                    grid[nr][nc] = grid[row][col] + 1
                    queue.append((nr,nc))