class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        
        res = [0] * len(temperatures)
        max_stack = []

        for idx, val in enumerate(temperatures):

            while max_stack and max_stack[-1][1] < val:
                res[max_stack[-1][0]] = idx - max_stack[-1][0]
                max_stack.pop()

            max_stack.append((idx,val))

        return res 