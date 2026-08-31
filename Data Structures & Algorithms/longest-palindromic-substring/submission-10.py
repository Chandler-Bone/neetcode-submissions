class Solution:
    def longestPalindrome(self, s: str) -> str:
        if len(s) == 1:
            return s

        res = [0,0]
        SLENGTH = len(s)

        for i in range(SLENGTH):
            
            #even pali check
            pl = pr = i

            while (
                pl in range(SLENGTH) and
                pr in range(SLENGTH) and
                s[pl] == s[pr]
            ):
                if (pr - pl) >= (res[1] - res[0]):
                    res = [pl,pr]

                pl -= 1
                pr += 1

            #odd pali check
            pl, pr = i, i + 1
            
            while (
                pl in range(SLENGTH) and
                pr in range(SLENGTH) and
                s[pl] == s[pr]
            ):
                if (pr - pl) >= (res[1] - res[0]):
                    res = [pl,pr]

                pl -= 1
                pr += 1
            
        return s[res[0]:res[1]+1]