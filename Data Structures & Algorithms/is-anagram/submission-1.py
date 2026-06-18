class Solution:
    def isAnagram(self, s: str, t: str) -> bool:

        if(len(s) != len(t)):
            return False

        count_s = list([0] * 26)
        count_t = list([0] * 26)

        for i in range(len(s)):
            count_s[ord(s[i]) - ord('a')] += 1
            count_t[ord(t[i]) - ord('a')] += 1

        if(count_s == count_t):
            return True
        
        return False
