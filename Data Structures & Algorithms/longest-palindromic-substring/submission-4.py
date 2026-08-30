class Solution:
    def longestPalindrome(self, s: str) -> str:
        
        longest = [0,0]

        for i in range(len(s)):

            # if even
            lp = i
            rp = i + 1

            while (
                lp in range(len(s)) and 
                rp in range(len(s)) and 
                s[lp] == s[rp]
            ):
                if (rp - lp) + 1 > (longest[1] - longest[0]) + 1:
                    longest = [lp,rp]
                lp -= 1
                rp += 1


            # if odd
            lp = i
            rp = i
            while (
                lp in range(len(s)) and 
                rp in range(len(s)) and 
                s[lp] == s[rp]
            ):
                if (rp - lp) + 1 > (longest[1] - longest[0]) + 1:
                    longest = [lp,rp]
                lp -= 1
                rp += 1

        return s[longest[0]:longest[1] + 1]
