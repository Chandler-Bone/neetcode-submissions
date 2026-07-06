class Solution:
    def minWindow(self, s: str, t: str) -> str:
        
        if len(t) > len(s):
            return ""

        s_count = defaultdict(int)
        t_count = defaultdict(int)

        for c in t:
            t_count[c] += 1
        
        matches = 0
        target_matches = len(t_count)

        res = ""
        res_length = float('inf')

        l = 0
        for r in range(len(s)):
            s_count[s[r]] += 1
            if s_count[s[r]] == t_count[s[r]]:
                matches += 1
            
            while matches == target_matches:
                if res_length > (r - l) + 1:
                    res_length = (r - l) + 1
                    res = s[l:r + 1]
                
                if s_count[s[l]] == t_count[s[l]]:
                    matches -= 1
                
                s_count[s[l]] -= 1
                l += 1

        return res