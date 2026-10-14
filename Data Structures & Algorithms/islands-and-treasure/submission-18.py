class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        
        LAND = 2147483647
        visited = set()
        queue = deque()
        directions = [[1,0], [-1,0], [0,1], [0,-1]]
        ROWS = len(grid)
        COLS = len(grid[0])

        for row in range(ROWS):
            for col in range(COLS):
                if grid[row][col] == 0:
                    queue.append((row,col,0))
                    visited.add((row,col))

        while queue:
            row, col, dist = queue.popleft()
            grid[row][col] = dist

            for x,y in directions:
                if(
                    0 <= row + x < ROWS and
                    0 <= col + y < COLS and
                    grid[row+x][col+y] != -1 and
                    (row + x, col + y) not in visited
                ):
                    queue.append((row + x, col + y, dist + 1))
                    visited.add((row + x, col + y))