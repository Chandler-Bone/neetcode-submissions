class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        
        l = 1
        r = max(piles)

        while l <= r:
            eating_rate = l + (r - l) // 2

            total_hours = 0
            for p in piles:
                total_hours += math.ceil(p/eating_rate)
            
            if(total_hours > h):
                l = eating_rate + 1
            else:
                r = eating_rate - 1

        return l