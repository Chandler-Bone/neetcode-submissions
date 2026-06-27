class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        
        l = 1
        r = max(piles)

        while l <= r:
            m = l + (r - l) // 2
            print(l)
            print(r)
            print(m)
            print("---")

            finish_time = 0
            for p in piles:
                finish_time += math.ceil(p / m)

            if (finish_time > h):
                l = m + 1
            elif (finish_time < h):
                r = m - 1
            else:
                r = m - 1
            
        return l