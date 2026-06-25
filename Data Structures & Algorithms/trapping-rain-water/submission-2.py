class Solution:
    def trap(self, height: List[int]) -> int:
        
        total = 0
        a = 0
        b = len(height) - 1
        max_a = 0
        max_b = 0

        while a < b:
            if height[a] < height[b]:
                if(height[a] > max_a):
                    max_a = height[a]
                else:
                    total += max_a - height[a]
                a += 1
            else:
                if(height[b] > max_b):
                    max_b = height[b]
                else:
                    total += max_b - height[b]
                b -= 1

        return total