class TrieNode:
    def __init__(self):
        self.children = {}
        self.word = False

class Solution:

    def __init__(self):
        self.root = TrieNode()

    def addWord(self, word):
        curr_node = self.root

        for c in word:
            if c not in curr_node.children:
                curr_node.children[c] = TrieNode()
            curr_node = curr_node.children[c]
        curr_node.word = True

    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        
        for word in words:
            self.addWord(word)

        ROWS, COLS = len(board), len(board[0])
        res, visited = set(), set()

        def dfs(row, col, node, word):
            if (not 0 <= row < ROWS or 
                not 0 <= col < COLS or 
                (row, col) in visited or 
                board[row][col] not in node.children
            ):
                return

            visited.add((row, col))
            node = node.children[board[row][col]]
            word += board[row][col]
            if node.word:
                res.add(word)

            dfs(row + 1, col, node, word)
            dfs(row - 1, col, node, word)
            dfs(row, col + 1, node, word)
            dfs(row, col - 1, node, word)
            visited.remove((row, col))

        for row in range(ROWS):
            for col in range(COLS):
                dfs(row, col, self.root, "")

        return list(res)

        