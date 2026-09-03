class Solution:
    def numDecodings(self, s: str) -> int:
        
        smap = {len(s) : 1}

        def dfs(i):
            if i in smap:
                return smap[i]
            if i >= len(s) or s[i] == "0":
                return 0
            
            count = dfs(i + 1)
            if i+1 < len(s) and int(s[i:i+2]) <= 26:
                count += dfs(i + 2)

            smap[i] = count
            return count

        return dfs(0)