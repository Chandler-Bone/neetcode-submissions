class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        
        ROWS, COLS = len(grid), len(grid[0])

        def distTreasure(r, c):
            visited = set()
            visited.add((r, c))
            queue = deque([[r, c]])
            # dist = 0
            directions = [[1,0], [-1,0], [0,1], [0,-1]]

            while queue:
                row, col = queue.popleft()

                # dist += 1
                for rd, cd in directions:
                    nr, nc = row + rd, col + cd
                    if (
                        nr in range(ROWS) and
                        nc in range(COLS) and
                        (nr, nc) not in visited and
                        grid[row][col] + 1 < grid[nr][nc]
                    ):
                        grid[nr][nc] = grid[row][col] + 1
                        visited.add((nr,nc))
                        queue.append([nr,nc])
        
        for row in range(ROWS):
            for col in range(COLS):
                if grid[row][col] == 0:
                    distTreasure(row, col)