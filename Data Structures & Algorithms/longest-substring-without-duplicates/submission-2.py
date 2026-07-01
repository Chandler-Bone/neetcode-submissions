class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        
        chars = set()
        res = 0
        low = 0

        for c in s:
            while c in chars:
                chars.remove(s[low])
                low += 1
            
            chars.add(c)
            res = max(res, len(chars))

        return res
