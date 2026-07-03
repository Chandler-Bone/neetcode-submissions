class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        
        l = 0
        max_freq = 0
        max_dist = 0
        count = [0] * 26

        for r in range(len(s)):

            r_idx = ord(s[r]) - ord('A')
            count[r_idx] += 1
            max_freq = max(max_freq, count[r_idx])

            while r - l + 1 > k + max_freq:
                count[ord(s[l]) - ord('A')] -= 1
                l += 1

            max_dist = max(max_dist, r - l + 1)

        return max_dist