class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:

        ROWS, COLS = len(heights), len(heights[0])
        atlantic, pacific = set(), set()
        res = []

        def checkWater(r, c):
            queue = deque([(r,c)])
            visited = set()
            visited.add((r,c))
            directions = [[1,0], [-1,0], [0,1], [0,-1]]

            while queue:
                row, col = queue.popleft()
                curr_height = heights[row][col]
                # check if on pacific tile
                if(row == 0 or col == 0):
                    pacific.add((r,c))
                # check if on atlantic tile
                if(row == ROWS - 1 or col == COLS - 1):
                    atlantic.add((r,c))
                
                if( (r,c) in pacific and (r,c) in atlantic):
                    break

                for rd, cd in directions:
                    nr, nc = row + rd, col + cd

                    if(
                        nr not in range(ROWS) or 
                        nc not in range(COLS)
                    ):
                        continue
                    # we should check if we have visited the tile already
                    # is this tile part of the atlantic or pacific? if so and our max_height is larger
                    if (
                        heights[nr][nc] <= curr_height and
                        (nr,nc) in atlantic and
                        (nr,nc) in pacific 
                    ):
                        pacific.add((r,c))
                        atlantic.add((r,c))
                        queue.clear()
                    elif(
                        (nr,nc) not in visited and
                        heights[nr][nc] <= curr_height
                    ):
                        queue.append((nr,nc))
                        visited.add((nr,nc))

            if (
                (r,c) in pacific and 
                (r,c) in atlantic
            ):
                res.append([r,c])
                

        for row in range(ROWS):
            for col in range(COLS):
                checkWater(row,col)

        return res
