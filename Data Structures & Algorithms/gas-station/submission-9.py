class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        
        if sum(gas) - sum(cost) < 0:
            return -1

        curr_val = 0
        max_val = float('-inf')
        max_idx = -1
        for i in range(len(gas) - 1, -1, -1):
            curr_val += (gas[i] - cost[i])
            if curr_val > max_val:
                max_idx = i
                max_val = curr_val

        return max_idx