class Solution:
    def isPalindrome(self, s: str) -> bool:
        l = 0
        r = len(s) - 1

        while l < r:
            if not isAlphaNum(s[l]):
                l += 1
                continue
            if not isAlphaNum(s[r]):
                r -= 1
                continue
            
            if s[l].lower() != s[r].lower():
                return False
            
            l += 1
            r -= 1
        return True


def isAlphaNum(c):
    if (ord("A") <= ord(c) <= ord("Z")) or \
        (ord("a") <= ord(c) <= ord("z")) or \
        (ord("0") <= ord(c) <= ord("9")):
        return True
    return False