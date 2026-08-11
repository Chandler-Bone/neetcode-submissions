class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        
        visited = set()
        ROWS, COLS = len(grid), len(grid[0])
        count = 0
        directions = [[1,0], [-1,0], [0,1], [0,-1]]

        def checkIsland(r, c):
            queue = deque([(r, c)])
            
            visited.add((r, c))
            while queue:
                row, col = queue.popleft()

                for dr, dc in directions:
                    if (
                        (row + dr) in range(ROWS) and
                        (col + dc) in range(COLS) and
                        (row + dr, col + dc) not in visited and
                        grid[row + dr][col + dc] == "1"
                    ):
                        visited.add((row + dr, col + dc))
                        queue.append((row + dr, col + dc))

        for row in range(ROWS):
            for col in range(COLS):
                if grid[row][col] == "1" and (row, col) not in visited:
                    checkIsland(row, col)
                    count += 1

        return count