class Solution:
    def trap(self, height: List[int]) -> int:
        
        l = 0
        r = len(height) - 1

        max_l = height[l]
        max_r = height[r]

        total_area = 0

        while l < r:

            if max_l < max_r:
                l += 1
                if height[l] < max_l and l != r:
                    total_area += max_l - height[l]
                else:
                    max_l = max(max_l, height[l])
            else:
                r -= 1
                if height[r] < max_r and l != r:
                    total_area += max_r - height[r]
                else:
                    max_r = max(max_r, height[r])
        
        return total_area