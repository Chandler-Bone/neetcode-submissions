class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        
        visited = set()
        ROWS, COLS = len(grid), len(grid[0])
        count = 0

        def checkIsland(row, col):
            if not 0 <= row < ROWS or not 0 <= col < COLS or (row,col) in visited or grid[row][col] == "0":
                return
            
            visited.add((row,col))
            checkIsland(row + 1, col)
            checkIsland(row - 1, col)
            checkIsland(row, col + 1)
            checkIsland(row, col - 1)

        for row in range(ROWS):
            for col in range(COLS):
                if grid[row][col] == "1" and (row, col) not in visited:
                    checkIsland(row, col)
                    count += 1
                # print(visited)

        return count