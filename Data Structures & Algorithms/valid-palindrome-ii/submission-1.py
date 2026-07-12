class Solution:
    def validPalindrome(self, s: str) -> bool:
        l = 0
        r = len(s) - 1

        while l < r:
            if s[l] != s[r]:
                skip_l = s[l+1:r+1]
                skip_r = s[l:r]
                if skip_l != skip_l[::-1] and skip_r != skip_r[::-1]:
                    return False
                else:
                    return True
            l += 1
            r -= 1

        return True