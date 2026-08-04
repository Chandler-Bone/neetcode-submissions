class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []

        def dfs(s, opn, cls):
            if cls == n:
                res.append(s)
            
            if opn < n:
                dfs(s + "(", opn + 1, cls)
            if cls < opn:
                dfs(s + ")", opn, cls + 1)

        dfs("", 0, 0)

        return res
