class Solution:
    def minWindow(self, s: str, t: str) -> str:
        
        if len(t) > len(s):
            return ""

        t_count = defaultdict(int)
        s_count = defaultdict(int)

        for c in t:
            t_count[c] += 1

        matches = 0
        for i in range(len(t)):
            c = s[i]
            if c in t_count.keys():
                s_count[c] += 1
                if s_count[c] == t_count[c]:
                    matches += 1

        if matches == len(t_count):
            return s[0:len(t)]

        print(matches)
        print(t_count)
        print(s_count)

        l = 0
        res = [0,1001]
        for r in range(len(t), len(s)):
            l_char = s[l]
            r_char = s[r]
            print(l)
            print(r)
            print("+++")
            
            if r_char in t_count:
                s_count[r_char] += 1
                if s_count[r_char] == t_count[r_char]:
                    matches += 1
            
            while matches == len(t_count) and l < len(s):
                l_char = s[l]
                if r - l < res[1] - res[0]:
                    res = [l,r]
                if l_char in t_count:
                    s_count[l_char] -= 1
                    if s_count[l_char] == t_count[l_char] - 1:
                        matches -= 1
                l += 1

        return s[res[0]: res[1] + 1] if res[1] < 1001 else ""