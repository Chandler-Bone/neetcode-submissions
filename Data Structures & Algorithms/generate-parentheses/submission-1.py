class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        
        res = []

        def dfs(curr, opn, cls):
            if cls == n:
                res.append(curr)
                return 

            if opn < n:
                dfs(curr + "(", opn + 1, cls)

            if opn > cls:
                dfs(curr + ")", opn, cls + 1)

        
        dfs("", 0, 0)
        return res