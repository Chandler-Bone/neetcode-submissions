class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        
        s1_count = [0] * 26
        s2_count = [0] * 26

        if len(s1) > len(s2):
            return False

        for c in s1:
            s1_count[ord(c) - ord('a')] += 1

        matches = 0

        for i in range(26):
            if s1_count[i] == 0:
                matches += 1
        
        l = 0
        r = 0
        while r < len(s2):

            # print(s2[l])
            # print(s2[r])
            r_char_idx = ord(s2[r]) - ord('a')
            l_char_idx = ord(s2[l]) - ord('a')

            s2_count[r_char_idx] += 1
            if s2_count[r_char_idx] == s1_count[r_char_idx]:
                matches += 1

            if matches == 26:
                return True

            if r >= len(s1) - 1:
                if s2_count[l_char_idx] == s1_count[l_char_idx]:
                    matches -= 1
                s2_count[l_char_idx] -= 1
                l += 1
            r += 1

        return False
