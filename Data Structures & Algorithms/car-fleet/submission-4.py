class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        
        fleets = 0
        pos_ctime = []

        for i in range(len(position)):
            pos_ctime.append((position[i], (target - position[i])/speed[i]))

        pos_ctime = sorted(pos_ctime)[::-1]

        stack = []

        for pos, ctime in pos_ctime:
            if not stack or stack[-1] < ctime:
                stack.append(ctime)
        
        return len(stack)