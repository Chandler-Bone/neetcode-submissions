class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        
        stack = []
        res = 0

        for i in range(len(heights)):
            
            start = i

            while stack and stack[-1][0] > heights[i]:
                prev_val, prev_idx = stack.pop()
                start = prev_idx
                res = max(res, (i - prev_idx) * prev_val)
            
            stack.append((heights[i], start))

        while stack:
            prev_val, prev_idx = stack.pop()
            res = max(res, (len(heights) - prev_idx) * prev_val)

        return res