class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        
        l = 1
        r = max(piles)

        while l < r:
            m = l + (r - l) // 2

            eat_time = 0
            for p in piles:
                eat_time += math.ceil(p/m)

            if eat_time > h:
                l = m + 1
            else:
                r = m

        return l