class Solution:
    def longestPalindrome(self, s: str) -> str:
        
        lpal = ""

        for i in range(len(s)):

            p1 = i 
            p2 = i 
            while (
                p1 >= 0 and
                p2 < len(s) and
                s[p1] == s[p2]
            ):
                if len(lpal) < (p2 - p1) + 1:
                    lpal = s[p1:p2+1]
                p1 -= 1
                p2 += 1
            
            p1 = i
            p2 = i + 1
            while (
                p1 >= 0 and
                p2 < len(s) and
                s[p1] == s[p2]
            ):
                if len(lpal) < (p2 - p1) + 1:
                    lpal = s[p1:p2+1]
                p1 -= 1
                p2 += 1
        
        return lpal
