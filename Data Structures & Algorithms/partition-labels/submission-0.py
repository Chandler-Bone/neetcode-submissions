class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        
        count = defaultdict(int)

        for i in s:
            count[i] += 1

        curr_chars = set()

        res = []
        start = -1
        for i in range(len(s)):
            curr_chars.add(s[i])
            count[s[i]] -= 1
            if(count[s[i]] == 0):
                curr_chars.remove(s[i])
            
            if(len(curr_chars) == 0):
               res.append(i-start)
               start = i

        return res