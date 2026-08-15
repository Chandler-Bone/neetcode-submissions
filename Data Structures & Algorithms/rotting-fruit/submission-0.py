class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        
        ROWS, COLS = len(grid), len(grid[0])
        queue = deque()
        directions = [[1,0], [-1,0], [0,1], [0,-1]]

        for row in range(ROWS):
            for col in range(COLS):
                if grid[row][col] == 2:
                    queue.append((row,col,0))

        max_time = 0
        while queue:
            row, col, time = queue.popleft()

            for rd, cd in directions:
                nr, nc = row + rd, col + cd
                if(
                    nr in range(ROWS) and
                    nc in range(COLS) and
                    grid[nr][nc] == 1
                ):
                    grid[nr][nc] = 2
                    queue.append((nr,nc,time+1))
                    max_time = max(max_time, time+1)

        for row in range(ROWS):
            for col in range(COLS):
                if grid[row][col] == 1:
                    return -1
        
        return max_time

