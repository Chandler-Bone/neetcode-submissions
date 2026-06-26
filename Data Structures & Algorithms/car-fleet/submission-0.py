class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        
        fleets = 0
        pos_ctime = []

        for i in range(len(position)):
            ctime = (target - position[i]) / speed[i]
            pos_ctime.append((position[i],ctime))
        
        pos_ctime = sorted(pos_ctime)

        fleet_stack = []
        max_val = float('-inf')
        print(pos_ctime)
        for i in range(len(pos_ctime) - 1, -1 , -1):
            if(pos_ctime[i][1] > max_val):
                max_val = pos_ctime[i][1]
                fleets += 1
            

        return fleets