class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        
        visited = set()
        ROWS, COLS = len(grid), len(grid[0])
        count = 0

        def checkIsland(row, col):
            queue = deque([(row, col)])
            
            while queue:
                prow, pcol = queue.popleft()
                
                if not 0 <= prow < ROWS or \
                    not 0 <= pcol < COLS or \
                    (prow,pcol) in visited or \
                    grid[prow][pcol] == "0":
                    continue
            
                visited.add((prow, pcol))
                queue.append((prow + 1, pcol))
                queue.append((prow - 1, pcol))
                queue.append((prow, pcol + 1))
                queue.append((prow, pcol - 1))

        for row in range(ROWS):
            for col in range(COLS):
                if grid[row][col] == "1" and (row, col) not in visited:
                    checkIsland(row, col)
                    count += 1

        return count