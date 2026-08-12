class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        
        visited = set()
        ROWS, COLS = len(grid), len(grid[0])
        self.max_area = 0
        directions = [[1,0], [-1,0], [0,1], [0,-1]]

        def getIslandSize(r, c):
            total_area = 0
            queue = deque([(r,c)])
            visited.add((r,c))

            while queue:
                row, col = queue.popleft()
                total_area += 1

                for rd, cd in directions:
                    if (
                        row + rd in range(ROWS) and
                        col + cd in range(COLS) and
                        (row + rd, col + cd) not in visited and
                        grid[row + rd][col + cd] == 1
                    ):
                        queue.append((row + rd, col + cd))
                        visited.add((row + rd, col + cd))

            self.max_area = max(self.max_area, total_area)


        for row in range(ROWS):
            for col in range(COLS):
                if (
                    (row,col) not in visited and
                    grid[row][col] == 1
                ):
                    getIslandSize(row, col)

        return self.max_area