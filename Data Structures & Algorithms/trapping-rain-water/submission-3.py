class Solution:
    def trap(self, height: List[int]) -> int:
        total = 0
        
        l = 0
        r = len(height) - 1

        max_l = height[l]
        max_r = height[r]

        while l < r:
            min_height = min(max_l, max_r)
            print(str(max_l) + " - " + str(max_r))
            print(str(height[l]) + " - " + str(height[r]))
            print(min_height)
            print(total)
            if(height[l] < height[r]):
                l += 1
                if(height[l] > max_l):
                    max_l = height[l]
                    print("blah left")
                else:
                    total += min_height - height[l]
                
            else:
                r -= 1
                if(height[r] > max_r):
                    print("blah right")
                    max_r = height[r]
                else:
                    total += min_height - height[r]
                
        return total