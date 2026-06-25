class Solution:
    def trap(self, height: List[int]) -> int:
        total = 0
        
        l = 0
        r = len(height) - 1

        max_l = height[l]
        max_r = height[r]

        while l < r:
            if(height[l] < height[r]):
                l += 1
                if(height[l] > max_l):
                    max_l = height[l]
                else:
                    total += max_l - height[l]
                
            else:
                r -= 1
                if(height[r] > max_r):
                    max_r = height[r]
                else:
                    total += max_r - height[r]
                
        return total