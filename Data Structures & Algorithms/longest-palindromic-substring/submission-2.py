class Solution:
    def longestPalindrome(self, s: str) -> str:
        
        longest = ""

        for i in range(len(s)):

            # if even
            lp = i
            rp = i + 1

            while (
                lp in range(len(s)) and 
                rp in range(len(s)) and 
                s[lp] == s[rp]
            ):
                if len(s[lp:rp+1]) > len(longest):
                    longest = s[lp:rp+1]
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
                if len(s[lp:rp+1]) > len(longest):
                    longest = s[lp:rp+1]
                lp -= 1
                rp += 1

        return longest
