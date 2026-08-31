class Solution:
    def countSubstrings(self, s: str) -> int:
        if len(s) == 1:
            return 1

        count = 0

        for i in range(len(s)):
            count += 1

            #even check
            pl, pr = i, i + 1
            while(
                pl in range(len(s)) and
                pr in range(len(s)) and
                s[pl] == s[pr]
            ):
              count += 1
              pl -= 1
              pr += 1  

            #odd check
            pl, pr = i - 1, i + 1
            while(
                pl in range(len(s)) and
                pr in range(len(s)) and
                s[pl] == s[pr]
            ):
              count += 1
              pl -= 1
              pr += 1  


        return count