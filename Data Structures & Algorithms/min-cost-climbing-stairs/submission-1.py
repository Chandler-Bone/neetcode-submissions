class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        
        val1 = cost[0]
        val2 = cost[1]

        for i in range(2, len(cost), 1):
            # print("check: " + str(val1) + " - " + str(val2))
            temp = val2
            val2 = min(val1,val2) + cost[i]
            val1 = temp
            # print("end: " + str(val1) + " - " + str(val2))

        return min(val1,val2)