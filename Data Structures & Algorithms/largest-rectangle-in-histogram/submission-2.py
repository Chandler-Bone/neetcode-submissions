class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:

        stack = []
        max_area = 0

        for idx, val  in enumerate(heights):
            norm_idx = idx
            # print(stack)
            # print(max_area)
            # print(str(idx) + " - " + str(val))
            while stack and stack[-1][1] > val:
                i_val = stack.pop()
                norm_idx = i_val[0]
                max_area = max(max_area, (idx - i_val[0]) * i_val[1])
            
            if not stack:
                stack.append((norm_idx,val))
            elif stack and stack[-1][1] < val:
                stack.append((norm_idx,val))

        while stack:
            # print(stack)
            i_val = stack.pop()
            max_area = max(max_area, (len(heights) - i_val[0]) * i_val[1])

        return max_area