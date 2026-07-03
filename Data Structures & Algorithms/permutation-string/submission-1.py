class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:

        char_list1 = [0] * 26
        char_list2 = [0] * 26

        if len(s2) < len(s1):
            return False

        for i in s1:
            char_list1[ord(i) - ord('a')] += 1

        for r in range(len(s2)):
            l = r - (len(s1) - 1) if r >= len(s1) - 1 else 0
            
            char_list2[ord(s2[r]) - ord('a')] += 1
            if l > 0:
                char_list2[ord(s2[l - 1]) - ord('a')] -= 1

            if char_list1 == char_list2:
                return True

        return False

        


        