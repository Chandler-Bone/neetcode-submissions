class Solution:
    def numDecodings(self, s: str) -> int:

        dp = {len(s) : 1}

        def dfs(i):
            if i in dp:
                return dp[i]
            if s[i] == "0":
                return 0

            count = dfs(i + 1)
            if len(s) - i >= 2 and int(s[i:i+2]) <= 26:
                count += dfs(i + 2)

            dp[i] = count
            return count


        return dfs(0)