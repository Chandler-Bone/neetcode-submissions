class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        
        l = 1
        r = max(piles)

        while l <= r:
            m = l + (r - l) // 2
            print(l)
            print(r)
            print(m)
            print("+++")

            eat_ctime = 0
            for p in piles:
                eat_ctime += math.ceil(p/m)
            
            if eat_ctime > h:
                l = m + 1
            else:
                r = m - 1
            
        return l