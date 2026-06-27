class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        
        stack = []

        max_area = 0

        for idx, height in enumerate(heights):
            # print(stack)
            # print(max_area)
            start = idx

            while stack and height < stack[-1][1]:
                t_idx, t_height = stack.pop()
                start = t_idx
                max_area = max((idx - t_idx) * t_height, max_area)
            
            stack.append((start,height))

        while stack:
            t_idx, t_height = stack.pop()
            max_area = max((idx + 1 - t_idx) * t_height, max_area)

        return max_area
