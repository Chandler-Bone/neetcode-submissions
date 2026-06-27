
class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:

        stack = []
        max_area = 0

        for idx, val  in enumerate(heights):
            start = idx

            while stack and stack[-1][1] > val:
                s_idx, s_val = stack.pop()
                start = s_idx
                max_area = max(max_area, (idx - s_idx) * s_val)
            
            stack.append((start,val))

        while stack:
            s_idx, s_val = stack.pop()
            max_area = max(max_area, (len(heights) - s_idx) * s_val)

        return max_area