class Solution:
    def isAnagram(self, s: str, t: str) -> bool:

        if(len(s) != len(t)):
            return False

        count = list([0] * 26)

        for i in range(len(s)):
            count[ord(s[i]) - ord('a')] += 1
            count[ord(t[i]) - ord('a')] -= 1

        print(count)
        if(count == [0] * 26):
            return True
        
        return False
