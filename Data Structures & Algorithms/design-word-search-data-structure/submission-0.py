class TrieNode:
    
    def __init__(self):
        self.children = {}
        self.word = False

class WordDictionary:

    def __init__(self):
        self.root = TrieNode()

    def addWord(self, word: str) -> None:
        curr_node = self.root

        for c in word:
            if c not in curr_node.children:
                curr_node.children[c] = TrieNode()
            curr_node = curr_node.children[c]

        curr_node.word = True

    def search(self, word: str) -> bool:
        curr_node = self.root

        def dfs(node, word):
            if not node:
                return False
            if len(word) == 0:
                return node.word

            if word[0] == ".":
                for cnode in node.children.values():
                    if dfs(cnode, word[1:]):
                        return True
            else:
                if word[0] in node.children:
                    return dfs(node.children[word[0]], word[1:])
            return False

        return dfs(curr_node, word)