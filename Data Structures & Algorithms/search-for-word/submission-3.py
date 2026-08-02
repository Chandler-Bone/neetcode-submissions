class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        
        COLS, ROWS = len(board[0]), len(board)
        visited = set()

        def dfs(word, row, col):
            if not word:
                return True
            if not 0 <= row < ROWS or not 0 <= col < COLS:
                return False
            if (row, col) in visited:
                return False
            if word[0] != board[row][col]:
                return False

            word = word[1:]

            visited.add((row, col))
            # print(visited)

            if dfs(word, row - 1, col) or dfs(word, row + 1, col) or dfs(word, row, col - 1) or dfs(word, row, col + 1):
                return True
            visited.remove((row, col))

            return False

        for col in range(COLS):
            for row in range(ROWS):
                visited = set()
                if dfs(word, row, col):
                    return True

        return False
        