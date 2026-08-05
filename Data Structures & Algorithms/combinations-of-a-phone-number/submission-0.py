class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if not digits:
            return []
        res = []
        digitToChar = {
            "2": "abc",
            "3": "def",
            "4": "ghi",
            "5": "jkl",
            "6": "mno",
            "7": "qprs",
            "8": "tuv",
            "9": "wxyz",
        }

        def dfs(s, curr):
            if s == "":
                res.append("".join(curr))
                return

            for i in digitToChar[s[0]]:
                print(curr)
                curr.append(i)
                dfs(s[1:], curr)
                curr.pop()

        dfs(digits, [])

        return res