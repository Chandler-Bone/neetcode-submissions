class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        
        ROWS, COLS = len(board), len(board[0])
        visited = set()

        def backtrack(word, row, col):
            if not word:
                return True
            if not 0 <= row < ROWS or not 0 <= col < COLS:
                return False
            if (row, col) in visited:
                return False
            if board[row][col] != word[0]:
                return False

            visited.add((row, col))
            if backtrack(word[1:], row + 1, col) or \
                backtrack(word[1:], row - 1, col) or \
                backtrack(word[1:], row, col + 1) or \
                backtrack(word[1:], row, col - 1):
                return True
            visited.remove((row, col))

            return False

        for row in range(ROWS):
            for col in range(COLS):
                if backtrack(word, row, col):
                    return True

        return False