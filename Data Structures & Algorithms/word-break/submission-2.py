class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        dp = [False] * (len(s) + 1)
        dp[0] = True
        # print(dp)

        for i in range(len(s)):
            if dp[i] == False:
                continue

            for word in wordDict:
                if i + len(word) > len(dp):
                    continue
                if s[i:i + len(word)] == word:
                    # print(i + len(word))
                    dp[i + len(word)] = True

        # print(dp)
        return dp[-1]

