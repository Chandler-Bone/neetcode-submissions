class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        
        ROWS, COLS = len(grid), len(grid[0])

        max_area = 0

        def islandArea(r, c):
            queue = deque([[r,c]])
            grid[r][c] = 0
            total = 0
            directions = [[1,0], [-1,0], [0,1], [0,-1]]

            while queue:
                row, col = queue.popleft()
                total += 1

                for rd, cd in directions:
                    if(
                        row + rd in range(ROWS) and
                        col + cd in range(COLS) and
                        grid[row + rd][col + cd] == 1
                    ):
                        grid[row + rd][col + cd] = 0
                        queue.append([row + rd, col + cd])
            
            return total
        
        for row in range(ROWS):
            for col in range(COLS):
                if grid[row][col] == 1:
                    max_area = max(max_area, islandArea(row, col))

        return max_area