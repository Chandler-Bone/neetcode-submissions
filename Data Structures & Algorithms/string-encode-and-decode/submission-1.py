class Solution:

    def encode(self, strs: List[str]) -> str:
        res = ""

        for st in strs:
            res += str(len(st)) + "#"
            res += st
        
        return res

    def decode(self, s: str) -> List[str]:
        res = []
        p1 = 0
        while p1 < len(s):
            p2 = p1
            while s[p2] != "#":
                p2 += 1

            slen = int(s[p1:p2])
            word = s[p2 + 1: p2 + slen + 1]
            res.append(word)
            p1 = p2 + slen + 1
        
        return res
