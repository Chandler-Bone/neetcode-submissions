class Solution:
    def maxArea(self, heights: List[int]) -> int:
        
        largest_area = 0

        a = 0
        b = len(heights) - 1

        while a < b:
            curr_area = (min(heights[a], heights[b]) * (b - a))
            largest_area = max(largest_area, curr_area)

            if(heights[a] < heights[b]):
                a += 1
            elif(heights[a] > heights[b]):
                b -= 1
            else:
                a += 1



        return largest_area