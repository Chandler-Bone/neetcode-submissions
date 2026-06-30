class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        
        res = [0] * len(temperatures)
    
        # [(temp,index), ...]
        stack = []

        for i in range(len(temperatures)):
        
            while stack and stack[-1][0] < temperatures[i]:
                temp, idx = stack.pop()
                res[idx] = i - idx
            
            stack.append((temperatures[i], i))

        return res