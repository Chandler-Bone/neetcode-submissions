class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        
        fleets = 0
        pos_ctime = []

        for i in range(len(position)):
            ctime = (target - position[i]) / speed[i]
            pos_ctime.append((position[i],ctime))
        
        pos_ctime = sorted(pos_ctime)[::-1]
        stack = []

        for i in pos_ctime:
            if not stack or i[1] > stack[-1]:
                stack.append(i[1])
            
        return len(stack)