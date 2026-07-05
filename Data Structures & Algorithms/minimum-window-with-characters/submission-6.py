class Solution:
    def minWindow(self, s: str, t: str) -> str:
        
        if(len(t) > len(s)):
            return ""

        t_count = defaultdict(int)
        s_count = defaultdict(int)

        for c in t:
            t_count[c] += 1

        matches = 0
        match_target = len(t_count)

        l = 0
        r = 0

        res_length = float('inf')
        res = [-1, -1]

        while r < len(s):

            s_count[s[r]] += 1
            if s[r] in t_count and s_count[s[r]] == t_count[s[r]]:
                matches += 1

            while matches == match_target:
                if res_length > r - l + 1:
                    res_length = r - l + 1
                    res = [l, r]
                
                s_count[s[l]] -= 1
                if s[l] in t_count and s_count[s[l]] == t_count[s[l]] - 1:
                    matches -= 1
                l += 1

            r += 1

        return s[res[0]: res[1] + 1]