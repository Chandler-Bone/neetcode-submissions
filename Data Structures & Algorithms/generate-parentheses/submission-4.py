class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        
        res = []

        def backtrack(s, opn, cls):
            if cls == n:
                res.append(s)
                return

            if opn < n:
                backtrack(s + "(", opn + 1, cls)
            
            if opn > cls:
                backtrack(s + ")", opn, cls + 1)

        backtrack("", 0, 0)

        return res