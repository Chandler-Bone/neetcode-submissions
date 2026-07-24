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

        def dfs(node, word):
            if not node:
                return False
            if word == "":
                return node.word

            if word[0] == ".":
                for child_node in node.children.values():
                    if dfs(child_node, word[1:]):
                        return True
            elif word[0] in node.children:
                return dfs(node.children[word[0]], word[1:])

            return False

        return dfs(self.root, word)
                

        
