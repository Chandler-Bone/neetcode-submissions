class Solution:
    def trap(self, height: List[int]) -> int:
        
        l = 0
        r = len(height) - 1
        total = 0

        max_l, max_r = 0, 0

        while l <= r:

            print(str(l) + "][" + str(r) + "] total:" + str(total) + " max_l=" + str(max_l) + " max_r=" + str(max_r))



            if height[l] > max_l:
                max_l = height[l]
                l += 1
                continue
            if height[r] > max_r:
                max_r = height[r]
                r -= 1
                continue

            if max_l < max_r:
                total += min(max_l, max_r) - height[l]
                l += 1
            else:
                total += min(max_l, max_r) - height[r]
                r -= 1


        return total