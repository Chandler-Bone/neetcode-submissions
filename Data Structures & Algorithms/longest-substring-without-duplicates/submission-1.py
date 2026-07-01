class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        
        chars = set()
        res = 0
        low = 0

        for i in range(len(s)):
            while s[i] in chars:
                chars.remove(s[low])
                low += 1
            
            chars.add(s[i])
            res = max(res, len(chars))

        return res
